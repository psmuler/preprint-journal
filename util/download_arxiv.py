import urllib, urllib.request
from urllib.error import HTTPError
import datetime
import logging
import time
import os

logging.basicConfig(
    filename='log/arxiv_log.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def download_arxiv_xml_date(
        path,
        date_from="20230101",
        date_to="20240101",
        page=0,
        page_size=100
    ):
    date_from = date_from.replace("-", "")
    date_to = date_to.replace("-", "")

    url = (
        f'https://export.arxiv.org/api/query'
        f'?search_query=submittedDate:[{date_from}0000+TO+{date_to}2359]'
        f'&start={page}&max_results={page_size}'
        f'&sortBy=submittedDate&sortOrder=ascending'
    )

    def fetch():
        return urllib.request.urlopen(url).read()

    try:
        content = fetch()
    except HTTPError as e:
        if e.code == 500:
            delay = 10 + int(10 * (time.time() % 1))  # 10–20 seconds
            logging.warning(
                f"HTTP 500 encountered for page {page}. "
                f"Retrying once after {delay} seconds."
            )
            time.sleep(delay)

            # second (and only) attempt
            try:
                content = fetch()
            except Exception:
                logging.error(
                    f"Second attempt failed for page {page}. Raising error."
                )
                raise
        else:
            raise

    # Save data
    with open(path, "wb") as f:
        f.write(content)

    # Count entries
    num_entries = content.count(b"</entry>")
    logging.info(f"Downloaded {num_entries} entries")

    # Continue or stop
    if num_entries == page_size:
        return page + page_size
    else:
        return None

def end_of_month(date_str):
    # one day before the first of the next month
    end_of_the_month = (datetime.datetime.strptime(date_str, "%Y%m%d") + datetime.timedelta(days=31)).replace(day=1) - datetime.timedelta(days=1)
    return end_of_the_month.strftime("%Y%m%d")

base_path = "data/arxiv_raw"

def daterange(start_date, end_date):
    """Yield each date between start_date and end_date inclusive."""
    for n in range((end_date - start_date).days + 1):
        yield start_date + datetime.timedelta(n)

if __name__ == "__main__":
    initial = {"year": 2021, "month": 8, "day": 29}
    # obtain day by day
    date = datetime.date(initial["year"], initial["month"], initial["day"])
    while date:
        if date > datetime.date(2021, 9, 14):
            break
        
        year = date.year
        month = date.month
        # Directory for this month
        out_path = f"{base_path}/{year}{month:02d}/"
        os.makedirs(out_path, exist_ok=True)
        
        # logging.info(f"Processing month {year}-{month:02d}")

        # --- DAILY LOOP ---
        date_from = date.strftime("%Y%m%d")
        date_to = date_from   # single day range

        logging.info(f"Downloading for {date_from} ...")

        page = 0
        while page is not None:
            logging.info(f"  Page {page} for date {date_from}")
            page = download_arxiv_xml_date(
                path=f"{out_path}arxiv_data_{date_from}_{page}.xml",
                date_from=date_from,
                date_to=date_to,
                page=page,
                page_size=1000
            )
            time.sleep(1)  # polite to servers

        # Move to next day
        date += datetime.timedelta(days=1)
