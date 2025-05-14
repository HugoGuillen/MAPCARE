#!/usr/bin/env python3
import os
import click
import pandas as pd
from src.analysis import plot_similarity_hist

@click.command()
@click.option('--input', required=True)
@click.option('--output', required=True)
def main(input, output):
    os.makedirs(output, exist_ok=True)
    df = pd.read_csv(input)
    plot_similarity_hist(df, os.path.join(output, 'similarity_hist.png'))

if __name__ == '__main__':
    main()
