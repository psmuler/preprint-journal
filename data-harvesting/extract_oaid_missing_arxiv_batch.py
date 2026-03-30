import polars as pl
from pathlib import Path

def extract_work_ids_and_dois_from_batches():
    paths = sorted(
        Path("out_batch_cursor").glob("works_batch_*.jsonl")
    )

    df = (
        pl.concat(
            [
                pl.scan_ndjson(p, schema={"id": pl.Utf8, "doi": pl.Utf8})
                .with_columns(
                    pl.col("id")
                    .str.replace("https://openalex.org/", "")
                    .alias("work_id"),
                    pl.col("doi").str.to_lowercase(),
                )
                .select(["work_id", "doi"])
                .unique()
                for p in paths
            ],
            how="vertical",
        )
    )
    return df

def detect_bad_inferred_doi():
    from pathlib import Path
    import polars as pl

    paths = sorted(Path("out_batch_cursor").glob("works_batch_*.jsonl"))

    bad = []
    missing = []
    for p in paths:
        try:
            s = pl.scan_ndjson(p).collect_schema()
            if "doi" not in s:
                missing.append(str(p))
            elif s["doi"] == pl.Null:
                bad.append(str(p))
        except Exception as e:
            bad.append(f"{p}  (scan failed: {type(e).__name__}: {e})")

    print("doi column missing:", len(missing))
    print("\n".join(missing[:20]))
    print("\ndoi column exists but inferred as Null:", len(bad))
    print("\n".join(bad[:20]))
    
    return bad, missing
    # output:
    # doi column missing: 0
    # doi column exists but inferred as Null: 77
    # out_batch_cursor/works_batch_2930.jsonl
    # out_batch_cursor/works_batch_2931.jsonl
    # out_batch_cursor/works_batch_2932.jsonl
    # out_batch_cursor/works_batch_2933.jsonl
    # out_batch_cursor/works_batch_2934.jsonl
    # out_batch_cursor/works_batch_2935.jsonl
    # out_batch_cursor/works_batch_2936.jsonl
    # out_batch_cursor/works_batch_2937.jsonl
    # out_batch_cursor/works_batch_2938.jsonl
    # out_batch_cursor/works_batch_2939.jsonl
    # out_batch_cursor/works_batch_2940.jsonl
    # out_batch_cursor/works_batch_2941.jsonl
    # out_batch_cursor/works_batch_2942.jsonl
    # out_batch_cursor/works_batch_2943.jsonl
    # out_batch_cursor/works_batch_2944.jsonl
    # out_batch_cursor/works_batch_2945.jsonl
    # out_batch_cursor/works_batch_2946.jsonl
    # out_batch_cursor/works_batch_2947.jsonl
    # out_batch_cursor/works_batch_2948.jsonl
    # out_batch_cursor/works_batch_2949.jsonl

if __name__ == "__main__":
    df = extract_work_ids_and_dois_from_batches()
    df.sink_parquet("arxiv_id_doi_2000-3076.parquet.zstd")
    # (
    #     pl.scan_ndjson("out_batch_cursor/works_batch_2930.jsonl")
    #     .head().collect(engine="streaming")
    #     .write_ndjson("sample_works_batch_2930.jsonl")
    # )

##### misc log and commands used #####
"""
cd data-harvesting/out_batch_cursor
  cat works_batch_{2001..3000}.jsonl \
  | gzip -1 \
  > ~/r2/works_batch_2001_3000.jsonl.gz

rclone move works_batch_0001_1000.jsonl.gz \
  r2:openalex/json/ \
  -P \
  --checksum

rclone move works_batch_0001_1000.jsonl.gz \
  r2:ec2/ \
  -P \
  --checksum
"""
# transferred to a wrong location...
# see it at r2:openalex/json/works_batch_0001_1000.jsonl.gz