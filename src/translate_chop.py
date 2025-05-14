#!/usr/bin/env python3
import click
import pandas as pd
from src.utils import remove_codes
from src.translation import create_model, translate_texts

@click.command()
@click.option('--input', 'infile', required=True)
@click.option('--output', 'outfile', required=True)
def main(infile, outfile):
    df = pd.read_csv(infile, encoding='utf-8-sig')
    df['clean_text'] = df['text'].apply(remove_codes)
    model = create_model('gemma2')
    raw = translate_texts(model, df['clean_text'].tolist())
    df['translation_raw'] = raw
    df.to_csv(outfile, index=False, encoding='utf-8-sig')

if __name__ == '__main__':
    main()
