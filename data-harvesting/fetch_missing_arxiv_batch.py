import json
import requests
from pathlib import Path
import glob
import polars as pl
import time
import logging

logging.basicConfig(
    filename="fetch_missing.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)

logger.info("Starting fetch_missing_arxiv_batch.py")
# ---------- 設定 ----------
CHUNK_SIZE = 1000
OUT_DIR = Path("out_batch_cursor")
OUT_DIR.mkdir(exist_ok=True)
BASE_URL = "https://api.openalex.org/works"

# ---------- バッファ ----------
buffer = []
file_idx = (
    max(
        [int(p.stem.split("_")[2]) for p in OUT_DIR.glob("works_batch_*.jsonl")],
        default=0,
    )
    + 1
)

def flush_buffer(buf, idx):
    path = OUT_DIR / f"works_batch_{idx:04d}.jsonl"
    with path.open("w", encoding="utf-8") as f:
        for record in buf:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

# ---------- メインループ ----------

flag = False
from tqdm import tqdm 

# cursor = "IlswLCAnLUluZmluaXR5JywgMCwgJ2h0dHBzOi8vb3BlbmFsZXgub3JnL1cyOTUxMzgwMzA5J10i"
# cursor = "IlswLCAnLUluZmluaXR5JywgMCwgJ2h0dHBzOi8vb3BlbmFsZXgub3JnL1c0Mjg3NzU4ODE1J10i"
# cursor = "IlswLCAnLUluZmluaXR5JywgMCwgJ2h0dHBzOi8vb3BlbmFsZXgub3JnL1c2ODkxODExNjExJ10i" # storage full -> json decode error
cursor = "IlswLCAnLUluZmluaXR5JywgMCwgJ2h0dHBzOi8vb3BlbmFsZXgub3JnL1c2OTI5NDAyNzk5J10i" 
while cursor:
    url = (
        f"{BASE_URL}"
        f"?filter=primary_location.source.id:s4306400194"
        "&per_page=100"
        "&sort=cited_by_count:desc"
        "&include_xpac=true"
        "&mailto=miura-tchiaki873@g.ecc.u-tokyo.ac.jp"
        f"&cursor={cursor}"
    )

    logger.info(f"Fetching cursor = {cursor}, buffer size = {len(buffer)}")
    try:
        r = requests.get(url, timeout=12)
        r.raise_for_status()
    except requests.ReadTimeout:
        logger.warning(f"Timeout fetching cursor = {cursor}, skipping.")
        continue
    except requests.HTTPError as e:
        if r.status_code // 100 == 4 or r.status_code // 100 == 5:
            if flag:
                logger.error("Subsequent HTTP error, stopping.")
                break
            flag = True

            logger.warning(f"{r.status_code} Error fetching cursor = {cursor}, sleeping and retrying.")
            time.sleep(600)
            r = requests.get(url, timeout=30)
            r.raise_for_status()
        else:
            logger.warning(f"Unexpected error {r.status_code} Error fetching cursor = {cursor}. Quitting")
            break

    data = r.json()
    buffer.extend(data.get("results", []))
    cursor = data.get("meta", {}).get("next_cursor", "")

    if len(buffer) >= CHUNK_SIZE:
        flush_buffer(buffer, file_idx)
        logger.info(f"latest: cursor = {cursor}, buffer size = {len(buffer)}")
        time.sleep(30)
        flag = False
        buffer.clear()
        file_idx += 1

# ---------- 端数 ----------
if buffer:
    flush_buffer(buffer, file_idx) 