#!/usr/bin/env python3
import click
import pandas as pd
from src.analysis import evaluate_semantic_alignment

@click.command()
@click.option('--map', 'mapfile', required=True)
@click.option('--output', required=True)
def main(mapfile, output):
    df = pd.read_csv(mapfile, sep='\t')
    eval_df = evaluate_semantic_alignment(df)
    eval_df.to_csv(output, index=False)

if __name__ == '__main__':
    main()
