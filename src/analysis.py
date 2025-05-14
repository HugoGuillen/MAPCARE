import matplotlib.pyplot as plt
import pandas as pd

def evaluate_semantic_alignment(df: pd.DataFrame) -> pd.DataFrame:
    """A simple rubric: label by similarity thresholds."""
    df['score'] = df['similarity']
    df['label'] = pd.cut(df['score'], bins=[-1, 0.5, 0.8, 1.0], labels=['poor','ok','good'])
    return df


def plot_similarity_hist(df: pd.DataFrame, output_path: str):
    """Histogram of similarity scores."""
    plt.figure()
    plt.hist(df['similarity'], bins=50)
    plt.xlabel('Cosine similarity')
    plt.ylabel('Count')
    plt.title('CHOP–OPS similarity distribution')
    plt.savefig(output_path)
    plt.close()
