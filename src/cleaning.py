import pandas as pd
from src.utils import clean_explanation

def clean_translations(df: pd.DataFrame) -> pd.DataFrame:
    """Split raw translations into structured columns."""
    records = [clean_explanation(raw) for raw in df['translation_raw']]
    trans, desc = zip(*records)
    df['translation'] = trans
    df['description'] = desc
    return df
