# MAP-CARE: Multilingual Approach for Procedures in Clinical and Retrieval Embeddings


Supporting code for the article **"MAP-CARE: Enhancing Cross-Lingual Medical Intervention Terms Analysis Through LLM-supported Semantic Embeddings"**

Hugo Guillen-Ramirez$^1$, Karen Triep$^2$, Guido Beldi$^1$ Olga Endrich$^{2,3}$

1 Department of Visceral Surgery and Medicine, Inselspital, Bern University Hospital, University of Bern, Bern, Switzerland
2 Medical Directorate, Medizincontrolling, Inselspital, University Hospital Bern, Insel Gruppe, Bern, Switzerland
3 Department of Clinical Chemistry, Inselspital, Bern University Hospital, University of Bern, Bern, Switzerland


1. **Translating** CHOP codes from German to English with medical explanations (using Ollama LLM).
2. **Cleaning** and parsing raw translation outputs into structured CSVs.
4. **Parsing** the OPS CLaML XML into a tabular hierarchy.
5. **Generating embeddings** for CHOP descriptions and OPS terms with Ollama & ChromaDB.
6. **Mapping** CHOP codes to OPS codes via cosine similarity.

## Quickstart

Check  [example.ipynb](example.ipynb)
