#!/usr/bin/env python3
import click
from src.mapping import map_embeddings

@click.command()
@click.option('--chop-vectors', required=True)
@click.option('--ops-vectors', required=True)
@click.option('--output', required=True)
@click.option('--top-k', type=int, default=5)
def main(chop_vectors, ops_vectors, output, top_k):
    df = map_embeddings(chop_vectors, ops_vectors, top_k)
    df.to_csv(output, sep='\t', index=False)

if __name__ == '__main__':
    main()
