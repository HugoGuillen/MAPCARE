import ollama

TRANSLATE_SYSTEM = (
    "Translate from German to English. Input text is clinical. "
    "Acronyms are medical/surgical. Include explanations. No greetings."
)

def create_model(chop_model: str, base: str = 'gemma2') -> str:
    """Build and register a custom Ollama model for translation."""
    modelfile = (
        f"FROM {base}\n"
        "PARAMETER temperature 0\n"
        f"SYSTEM {TRANSLATE_SYSTEM}\n"
        "MESSAGE user Example"
    )
    name = f'CHOP_{chop_model}'
    ollama.create(model=name, modelfile=modelfile)
    return name


def translate_texts(model: str, texts: list[str]) -> list[str]:
    """Batch translate texts via Ollama chat API."""
    results = []
    for t in texts:
        resp = ollama.chat(model=model, messages=[{'role':'user','content':t}])
        results.append(resp['message']['content'])
    return results
