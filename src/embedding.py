import time
import pandas as pd
import ollama
import chromadb
import pyarrow
from chromadb.utils import embedding_functions

def generate_embeddings(infile, out_vectors, out_corpus, model="mxbai-embed-large",OPS=False):
    df = pd.read_csv(infile).fillna('')
    df['corpus'] = df['translation']+' | '+df['description']
    start_time = time.time()
    rows = []
    N = len(df)
    for i, d in enumerate(df.corpus):    
        if (i+1)%100 == 0:
            print("%d/%d"%((i+1),N),flush=True)
        response = ollama.embeddings(model=model, prompt=d)
        embedding = response["embedding"]
        rows.append(embedding)
    end_time = time.time()
    elapsed_time = end_time - start_time
    time_per_term = elapsed_time/N
    print('Embedding s/term: %.2f'%time_per_term,flush=True)
    d = pd.DataFrame(rows)
    d.columns = [str(x) for x in d.columns]
    d.to_parquet(out_vectors)
    print('# Wrote',out_vectors,flush=True)
    if not OPS: #CHOP
        df['corpus'] = df['zcode']+'|'+df['item type']+'|'+df['translation']+'|'+df['description']
    else: #OPS
        df['corpus'] = df['code']+'|'+df['translation']+'|'+df['description']
    df[['corpus']].to_csv(out_corpus,index=None)
    print('# Wrote',out_corpus,flush=True)


def ingest_to_chroma(collection_name, embeddings_parquet,corpus_txt,persist_directory):
    """Store embeddings in a Chromadb collection."""    
    df = pd.read_parquet(embeddings_parquet)
    x = pd.read_csv(corpus_txt)
    client = chromadb.PersistentClient(path=persist_directory)
    col = client.get_or_create_collection(name=collection_name)
    col.add(ids=list(x.corpus), embeddings=df.values)
