import json
import requests
from pathlib import Path
import glob
import polars as pl
import time

arxiv_missing = pl.read_ndjson("arxiv_missing_preprints.jsonl")
arxiv_ids = arxiv_missing.select("doi").to_series().to_list()
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    filename="fetch_missing.log"
)

# ---------- 設定 ----------
CHUNK_SIZE = 1000
OUT_DIR = Path("out")
OUT_DIR.mkdir(exist_ok=True)

BASE_URL = "https://api.openalex.org/works"

# ---------- 既取得IDの復元 ----------
def load_already_fetched_ids(out_dir: Path) -> set[str]:
    fetched = set()
    for path in glob.glob(str(out_dir / "works_*.jsonl")):
        with open(path, encoding="utf-8") as f:
            for line in f:
                obj = json.loads(line)
                # OpenAlexの標準的な DOI 格納場所
                doi = obj.get("doi")
                if doi:
                    fetched.add(doi.lower().removeprefix("https://doi.org/"))
    return set(fetched)

already_fetched = load_already_fetched_ids(OUT_DIR)

logging.info(f"Already fetched: {len(already_fetched)}")

# ---------- バッファ ----------
buffer = []
file_idx = (
    max(
        [int(p.stem.split("_")[1]) for p in OUT_DIR.glob("works_*.jsonl")],
        default=0,
    )
    + 1
)

def flush_buffer(buf, idx):
    path = OUT_DIR / f"works_{idx:04d}.jsonl"
    with path.open("w", encoding="utf-8") as f:
        for record in buf:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

# ---------- メインループ ----------
arxiv_ids_filtered = set(arxiv_ids) - already_fetched
logging.info(f"To fetch: {len(arxiv_ids_filtered)}")

flag = False
from tqdm import tqdm 
for arxiv_id in tqdm(arxiv_ids_filtered):
    arxiv_id = arxiv_id.lower()

    url = (
        f"{BASE_URL}"
        f"?filter=doi_starts_with:{arxiv_id}"
        "&per_page=1"
        "&include_xpac=true"
        "&mailto=miura-tchiaki873@g.ecc.u-tokyo.ac.jp"
    )

    try:
        r = requests.get(url, timeout=3)
        r.raise_for_status()
    except requests.ReadTimeout:
        logging.warning(f"Timeout fetching {arxiv_id}, skipping.")
        time.sleep(10)
        continue
    except requests.HTTPError as e:
        if r.status_code == 503:
            logging.warning(f"503 Error fetching {arxiv_id}, sleeping and retrying.")
            time.sleep(600)
            r = requests.get(url, timeout=10)
            r.raise_for_status()
        else:
            if flag:
                logging.error("Subsequent HTTP error, stopping.")
                break
            flag = True
            time.sleep(600)
            logging.warning(f"HTTP error {r.status_code} fetching {arxiv_id}, skipping.")
            continue

    data = r.json()

    for work in data.get("results", []):
        buffer.append(work)
        doi = work.get("doi")
        if doi:
            already_fetched.add(doi.lower())

        if len(buffer) == CHUNK_SIZE:
            flush_buffer(buffer, file_idx)
            logging.info(f"latest: {arxiv_id}")
            time.sleep(60)
            flag = False
            buffer.clear()
            file_idx += 1

# ---------- 端数 ----------
if buffer:
    flush_buffer(buffer, file_idx)