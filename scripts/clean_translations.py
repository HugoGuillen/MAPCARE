#!/usr/bin/env python3
import click
import pandas as pd
from src.cleaning import clean_translations

@click.command()
@click.option('--input', 'infile', required=True)
@click.option('--output', 'outfile', required=True)
def main(infile, outfile):
    df = pd.read_csv(infile, encoding='utf-8-sig')
    clean_df = clean_translations(df)
    clean_df.to_csv(outfile, index=False, encoding='utf-8-sig')

if __name__ == '__main__':
    main()
