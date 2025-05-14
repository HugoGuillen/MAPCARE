import re

def remove_codes(text: str) -> str:
    """Strip parenthetical codes from a clinical text."""
    return re.sub(r"\([A-Za-z0-9.,\s-]+\)", '', text)


def clean_explanation(raw: str) -> tuple[str, str]:
    """Normalize LLM output into (translation, description)."""
    sep = '|' if '|' in raw else ('\n' if '\n' in raw else ' - ')
    parts = raw.split(sep, 1)
    translation = parts[0].strip()
    desc = parts[1].strip() if len(parts) > 1 else ''
    lines = [l.strip().lstrip('*').replace('Explanation:', '').strip() for l in desc.splitlines()]
    return translation, '\n'.join(filter(None, lines))
