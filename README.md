# CHOP-OPS Processing Pipeline

This repository provides a modular, reproducible pipeline for:

1. **Translating** CHOP codes from German to English with medical explanations (using Ollama LLM).
2. **Cleaning** and parsing raw translation outputs into structured CSVs.
3. **Generating embeddings** for CHOP descriptions and OPS terms with Ollama & ChromaDB.
4. **Mapping** CHOP codes to OPS codes via cosine similarity.
5. **Parsing** the OPS CLaML XML into a tabular hierarchy.
6. **Evaluating** semantic alignment of CHOP–OPS mappings with a simple rubric.
7. **Analyzing** performance and visualization of results.

## Quickstart

```bash
conda env create -f environment.yml
conda activate chop_pipeline
make all
```

Or run individual steps:
```bash
python scripts/translate_chop.py --input inputs/CHOP.csv --output outputs/translated.csv
python scripts/clean_translations.py --input outputs/translated.csv --output outputs/clean.csv
python scripts/embed_chop.py --input outputs/clean.csv --out-vectors outputs/embeddings_chop.parquet --out-corpus outputs/embeddings_chop.txt --persist-dir db
python scripts/map_chop_ops.py --chop-vectors outputs/embeddings_chop.parquet --ops-vectors outputs/embeddings_ops.parquet --output outputs/chop2ops.tsv
python scripts/parse_ops.py --input inputs/ops2023syst_claml.xml --abbv inputs/OPS_ABBV.tsv --output outputs/ops_parsed.csv
python scripts/evaluate_semantics.py --map outputs/chop2ops.tsv --output outputs/semantic_eval.csv
python scripts/analyze_results.py --input outputs/semantic_eval.csv --output figures/
```
