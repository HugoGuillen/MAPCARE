.PHONY: all translate clean embed map parse eval analyze
all: translate clean embed map parse eval analyze

translate:
	python scripts/translate_chop.py --input inputs/CHOP.csv --output outputs/translated.csv

clean:
	python scripts/clean_translations.py --input outputs/translated.csv --output outputs/clean.csv

embed:
	python scripts/embed_chop.py --input outputs/clean.csv --out-vectors outputs/embeddings_chop.parquet --out-corpus outputs/embeddings_chop.txt --persist-dir db

map:
	python scripts/map_chop_ops.py --chop-vectors outputs/embeddings_chop.parquet --ops-vectors outputs/embeddings_ops.parquet --output outputs/chop2ops.tsv

parse:
	python scripts/parse_ops.py --input inputs/ops2023syst_claml.xml --abbv inputs/OPS_ABBV.tsv --output outputs/ops_parsed.csv

eval:
	python scripts/evaluate_semantics.py --map outputs/chop2ops.tsv --output outputs/semantic_eval.csv

analyze:
	python scripts/analyze_results.py --input outputs/semantic_eval.csv --output figures/
