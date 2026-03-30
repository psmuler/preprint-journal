import json
import time
import logging
from pathlib import Path

import requests


logging.basicConfig(
    filename="log/fetch_crossref_preprints.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)
logger.info("Starting fetch_crossref_preprints.py")


# ======================
# 設定（ここを触れば動く）
# ======================
doi_prefix = "10.20944"  # ← ここを変える（例: "10.48550" など）
mailto = "miura-tchiaki873@g.ecc.u-tokyo.ac.jp"

# Crossrefは rows が最大1000 程度が現実的
ROWS = 1000
CHUNK_SIZE = 10000

OUT_DIR = Path(f"data/out_crossref_prefix_{doi_prefix.replace('.', '_')}")
OUT_DIR.mkdir(exist_ok=True)

BASE_URL = "https://api.crossref.org/v1/works"

# polite pool を意識した最低限の名乗り
HEADERS = {
    "User-Agent": f"preprint-metadata-harvester/0.1 (mailto:{mailto})"
}

# =========
# I/O
# =========
def flush_buffer(buf, idx: int) -> None:
    path = OUT_DIR / f"works_batch_{idx:04d}.jsonl"
    with path.open("w", encoding="utf-8") as f:
        for record in buf:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")


file_idx = (
    max(
        [int(p.stem.split("_")[-1]) for p in OUT_DIR.glob("works_batch_*.jsonl")],
        default=0,
    )
    + 1
)

buffer = []


# ==========================
# Crossref cursor deep paging
# ==========================
def request_with_backoff(session: requests.Session, params: dict, cursor: str) -> dict:
    """
    429や一時障害を想定して、指数バックオフ + Retry-After を尊重。
    """
    backoff = 2.0
    max_backoff = 600.0

    while True:
        try:
            r = session.get(BASE_URL, params=params, headers=HEADERS, timeout=60)
            if r.status_code == 429:
                ra = r.headers.get("Retry-After")
                sleep_s = float(ra) if ra and ra.isdigit() else backoff
                logger.warning(f"429 rate limited at cursor={cursor}. sleeping {sleep_s}s")
                time.sleep(sleep_s)
                backoff = min(max_backoff, backoff * 2.0)
                continue

            r.raise_for_status()
            return r.json()

        except requests.ReadTimeout:
            logger.warning(f"Timeout at cursor={cursor}. sleeping {backoff}s and retrying.")
            time.sleep(backoff)
            backoff = min(max_backoff, backoff * 2.0)

        except requests.HTTPError as e:
            status = getattr(r, "status_code", None)
            logger.warning(f"HTTPError {status} at cursor={cursor}: {e}. sleeping {backoff}s and retrying.")
            time.sleep(backoff)
            backoff = min(max_backoff, backoff * 2.0)

        except requests.RequestException as e:
            logger.warning(f"RequestException at cursor={cursor}: {e}. sleeping {backoff}s and retrying.")
            time.sleep(backoff)
            backoff = min(max_backoff, backoff * 2.0)


def main():
    global file_idx

    sess = requests.Session()

    params = {
        "filter": f"type:posted-content,prefix:{doi_prefix}",
        "rows": ROWS,
        "cursor": "*",
        "mailto": mailto,
        # "select": "DOI,title,author,created,posted,issued,resource,relation,link,type,container-title",
    }

    cursor = "*"

    while cursor:
        params["cursor"] = cursor

        logger.info(f"Fetching cursor={cursor}, buffer size={len(buffer)}, file_idx={file_idx}")

        data = request_with_backoff(sess, params, cursor)

        message = data.get("message", {})
        items = message.get("items", [])
        next_cursor = message.get("next-cursor", "")

        if not items:
            logger.info(f"No items returned at cursor={cursor}. stopping.")
            break

        buffer.extend(items)
        
        if len(items) < ROWS:
            logger.info(f"Fetched less than requested rows at cursor={cursor}. stopping.")
            break
        cursor = next_cursor

        if len(buffer) >= CHUNK_SIZE:
            flush_buffer(buffer, file_idx)
            logger.info(f"Flushed batch {file_idx:04d}. next_cursor={cursor}")
            buffer.clear()
            file_idx += 1

            # politeに少し間を置く（429が出るならここも増やす）
            time.sleep(0.2)

    if buffer:
        flush_buffer(buffer, file_idx)
        logger.info(f"Flushed final batch {file_idx:04d}.")
        


import polars as pl
if __name__ == "__main__":
    lf = pl.scan_ndjson("data/out_crossref_prefix_10_26434/*.jsonl")
    # print(lf.collect_schema())
    print(lf.count().collect(engine='streaming'))
    print(lf.unique("DOI").count().collect(engine='streaming'))

    # main()