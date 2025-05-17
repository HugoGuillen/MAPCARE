#!/usr/bin/env python3
import click
import pandas as pd
from src.embedding import generate_embeddings, ingest_to_chroma

# @click.command()
# @click.option('--input', 'infile', required=True)
# @click.option('--out-vectors', required=True)
# @click.option('--out-corpus', required=True)
# @click.option('--persist-dir', default='db')
def main(infile, out_vectors, out_corpus, persist_dir):    
    embeddings = generate_embeddings(infile, out_vectors, out_corpus,model="mxbai-embed-large",OPS=False)    
    ingest_to_chroma('chop', out_vectors,out_corpus,persist_dir)

if __name__ == '__main__':
    main()
