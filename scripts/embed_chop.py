#!/usr/bin/env python3
import click
import pandas as pd
from src.embedding import generate_embeddings, ingest_to_chroma

@click.command()
@click.option('--input', 'infile', required=True)
@click.option('--out-vectors', required=True)
@click.option('--out-corpus', required=True)
@click.option('--persist-dir', default='db')
def main(infile, out_vectors, out_corpus, persist_dir):
    df = pd.read_csv(infile, encoding='utf-8-sig')
    embeddings = generate_embeddings(df['translation'].tolist(), model='gemma2')
    df['embedding'] = embeddings
    df.to_parquet(out_vectors)
    df[['code','translation']].to_csv(out_corpus, index=False)
    ingest_to_chroma('chop', embeddings, df.to_dict('records'), df['code'].tolist(), persist_dir)

if __name__ == '__main__':
    main()
