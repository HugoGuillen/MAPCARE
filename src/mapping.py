import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def map_embeddings(chop_vectors_path: str,
                   ops_vectors_path: str,
                   top_k: int = 5) -> pd.DataFrame:
    """Compute top-k CHOP→OPS by cosine similarity."""
    chop_df = pd.read_parquet(chop_vectors_path)
    ops_df = pd.read_parquet(ops_vectors_path)
    sims = cosine_similarity(chop_df['embedding'].tolist(), ops_df['embedding'].tolist())
    records = []
    for i, row in enumerate(sims):
        best = row.argsort()[::-1][:top_k]
        for j in best:
            records.append({
                'chop_code': chop_df.iloc[i]['code'],
                'ops_code': ops_df.iloc[j]['code'],
                'similarity': row[j]
            })
    return pd.DataFrame(records)
