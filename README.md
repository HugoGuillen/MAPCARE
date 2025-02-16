# MAPCARE: Multilingual Approach for Procedures in Clinical and Retrieval Embeddings

This repository contains the new unified code for processing CHOP data. The script `process_chop.py` provides a command-line interface to either translate or generate extended explanations for the clinical texts in your CHOP CSV file.

## Repository Structure

```
MAPCARE/
├── process_chop.py       # Main processing script with CLI options
├── run_process.sh        # Sample SLURM batch script to run the process
├── README.md             # This file
├── requirements.txt      # Python dependencies
└── .gitignore            # Files/directories to ignore in git
```

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/MAPCARE.git
   cd MAPCARE
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure and start your Ollama service** as needed (see your existing setup).

## Usage

Run the script using the command line. For example:

- To translate:
  ```bash
  python process_chop.py --mode translate --input ~/data/chop.csv --output ~/outputs/translated.csv
  ```

- To generate extended explanations:
  ```bash
  python process_chop.py --mode extended --input ~/data/chop.csv --output ~/outputs/extended.csv
  ```

## SLURM Batch Script

Use the provided `run_process.sh` file to run the jobs on your cluster.
