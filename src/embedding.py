import ollama
import chromadb
from chromadb.utils import embedding_functions


def generate_embeddings(texts: list[str], model: str) -> list[list[float]]:
    """Return embeddings for a list of texts."""
    return ollama.embeddings(model=model, texts=texts)


def ingest_to_chroma(collection_name: str,
                     embeddings: list[list[float]],
                     metadatas: list[dict],
                     ids: list[str],
                     persist_directory: str):
    """Store embeddings in a Chromadb collection."""
    client = chromadb.Client()
    embed_fn = embedding_functions.OllamaEmbeddingFunction(model_name='gemma2')
    col = client.get_or_create_collection(name=collection_name, embedding_function=embed_fn)
    col.add(ids=ids, embeddings=embeddings, metadatas=metadatas)
    client.persist(persist_directory)
