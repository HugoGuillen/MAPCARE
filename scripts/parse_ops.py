#!/usr/bin/env python3
import click
from src.parsing_ops import parse_ops

# @click.command()
# @click.option('--input', 'xml', required=True)
# @click.option('--abbv', required=True)
# @click.option('--output', required=True)
def main(xml, abbv, output):
    parse_ops(xml, abbv, output)    

if __name__ == '__main__':
    main()
