import re


def clean_text(text: str) -> str:
    text = text.strip()
    text = text.strip('"').strip("'")
    return re.sub(r"\n{3,}", "\n\n", text)


def validate_inputs(purpose: str, recipient: str, key_points: str) -> list[str]:
    errors = []
    if not purpose or not purpose.strip():
        errors.append("Purpose is required.")
    if not recipient or not recipient.strip():
        errors.append("Recipient is required.")
    if not key_points or not key_points.strip():
        errors.append("At least one key point is required.")
    return errors


def word_count(text: str) -> int:
    return len(text.split())