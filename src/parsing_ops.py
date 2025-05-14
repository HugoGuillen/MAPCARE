import pandas as pd
from lxml import etree

def parse_ops(xml_path: str, abbv_path: str) -> pd.DataFrame:
    """Parse OPS CLaML XML into a flat table, merging abbreviations."""
    tree = etree.parse(xml_path)
    root = tree.getroot()
    records = []
    for entry in root.findall('.//section'):
        code = entry.get('code')
        title = entry.findtext('title')
        records.append({'ops_code': code, 'ops_title': title})
    df = pd.DataFrame(records)
    abbv = pd.read_csv(abbv_path, sep='\t')
    return df.merge(abbv, on='ops_code', how='left')
