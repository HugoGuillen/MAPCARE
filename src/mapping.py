import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def map_embeddings(book_A,book_B,top_k):
    """Compute top-k book A→book B by cosine similarity."""
    A_df = pd.read_parquet(book_A)
    B_df = pd.read_parquet(book_B)
    sims = cosine_similarity(A_df.values, B_df.values)
    records = []
    for i, row in enumerate(sims):
        best = row.argsort()[::-1][:top_k]
        for j in best:
            records.append({
                'A_df': i,
                'B_df': j,
                'similarity': row[j]
            })
    return pd.DataFrame(records)
