import glob
from xml.dom import minidom
import pathlib
import logging
import polars as pl
import os 
import tqdm

datadir = "data/arxiv_raw"
output_path = "/home/ec2-user/r2/arxiv"

logging.basicConfig(
    filename='log/arxiv_process.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def get_author_text(doc):
    """
    Inputs a minidom doc object, outputs a tuple of (string formatted list of authors, python list of authors).
    
    Helper function for doc_to_dict()
    
    """
    authorlist = []
    authortext = ""
    for author in doc.getElementsByTagName("authors")[0].childNodes:
        keyname = author.getElementsByTagName("keyname")[0].firstChild.data
        try:
            forenames = author.getElementsByTagName("forenames")[0].firstChild.data
        except:
            forenames = ""
        authortext += forenames + " " + keyname + ", "
        authorlist.append(forenames + " " + keyname)
    return authortext[:-2].replace("  ", " "), authorlist

def doc_to_dict(doc):
    """
    Inputs a minidom object, returns a dictionary of all metadata
    """

    title = doc.getElementsByTagName("title")[0].firstChild.data
    arxivid = doc.getElementsByTagName("id")[0].firstChild.data
    created = doc.getElementsByTagName("published")[0].firstChild.data
    created_ym = doc.getElementsByTagName("published")[0].firstChild.data[:7]
    categories = [cat.getAttribute("term") for cat in doc.getElementsByTagName("category")]
    abstract = doc.getElementsByTagName("summary")[0].firstChild.data
    primary_cat = doc.getElementsByTagName("arxiv:primary_category")[0].getAttribute("term")
    acm_categories = []
    msc_categories = []
    
    for cat in categories:
        if len(cat.split("."))==3:
            categories.remove(cat)
            acm_categories.append(cat)
        if len(cat.split("."))==0 and len(cat)==5:
            categories.remove(cat)
            msc_categories.append(cat)

    # author_text, author_list = get_author_text(doc)
    # num_authors = len(author_list)
    
    num_categories = len(categories)
    
    try:
        comments = doc.getElementsByTagName("arxiv:comment")[0].firstChild.data
    except IndexError:
        comments = None
        
    try:
        updated = doc.getElementsByTagName("updated")[0].firstChild.data
    except IndexError:
        updated = None
        
    try:
        doi = doc.getElementsByTagName("arxiv:doi")[0].firstChild.data
    except IndexError:
        doi = None         
        
    row = {
           'title':title,
           'updated':updated,
           'arxiv_id':arxivid,
           'created':created,
           'created_ym':created_ym,
           'categories':categories,
           'acm_categories':acm_categories,
           'msc_categories':msc_categories,
           'num_categories':num_categories,
           'primary_cat':primary_cat,
           'abstract':abstract,
           'doi':doi,
           'comments':comments,
        #    'author_text':author_text,
        #    'num_authors':num_authors
    }
    
    return row

def parse_meta(doc):
    """
    Inputs a minidom object, cleans a header tag, and returns a list of all metadata entries
    """
    entries = doc.getElementsByTagName("entry")
    return entries

def process_files(fn):
    df_list = []
    for file in tqdm.tqdm(fn):
        try:
            doc = minidom.parse(file)
            for entry in parse_meta(doc):
                # inspect the content of minidom
                row = doc_to_dict(entry)
                df_list.append(row)
        
        except IsADirectoryError:
            pass
    return df_list

def quick_check_files(df):
    if df.height != df.drop_nulls().height:
        logging.warning(f"DataFrame contains null rows. {df.height}, {df.drop_nulls().height}")
    if df.height != df.unique().height:
        logging.warning(f"DataFrame contains null or duplicate rows. {df.height}, {df.unique().height}")
    curated = df.group_by(pl.col("doi").is_null()).agg(pl.len()).to_dicts()
    logging.info(f"Curated vs non-curated counts:{curated}") # values of true and false


pathlib.Path(output_path).mkdir(parents=True, exist_ok=True) 

if __name__ == "__main__":
    for year in range(2019, 2024+1):
        year_df = pl.DataFrame()
        for month in range(1, 12+1):
            month_str = f"{year}{month:02d}"
            fn = glob.glob(f"{datadir}/{month_str}/*")
            df_list = process_files(fn)
            df = pl.DataFrame(df_list)
            quick_check_files(df)
            year_df = year_df.vstack(df)
    
        year_df.write_ndjson(f"{output_path}/full_{year}.jsonl")
