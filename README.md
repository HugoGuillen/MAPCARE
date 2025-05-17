MAP-CARE: Multilingual Approach for Procedures in Clinical and Retrieval Embeddings

This repository provides a modular, reproducible pipeline for:

1. **Translating** CHOP codes from German to English with medical explanations (using Ollama LLM).
2. **Cleaning** and parsing raw translation outputs into structured CSVs.
4. **Parsing** the OPS CLaML XML into a tabular hierarchy.
5. **Generating embeddings** for CHOP descriptions and OPS terms with Ollama & ChromaDB.
6. **Mapping** CHOP codes to OPS codes via cosine similarity.

## Quickstart

Check  [example.ipynb](example.ipynb)