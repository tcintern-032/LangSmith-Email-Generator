from langsmith import traceable
from langchain_core.output_parsers import StrOutputParser

from llm import get_llm
from prompts import email_prompt, subject_prompt
from utils import clean_text, validate_inputs

parser = StrOutputParser()


@traceable(name="generate_email_body")
def generate_email(
    purpose: str,
    recipient: str,
    key_points: str,
    tone: str = "professional",
    length: str = "medium (100-150 words)",
) -> str:
    errors = validate_inputs(purpose, recipient, key_points)
    if errors:
        raise ValueError("; ".join(errors))

    llm = get_llm(temperature=0.7)
    chain = email_prompt | llm | parser

    result = chain.invoke(
        {
            "purpose": purpose,
            "recipient": recipient,
            "tone": tone,
            "key_points": key_points,
            "length": length,
        },
        config={
            "tags": ["email-generation"],
            "metadata": {"tone": tone, "length": length},
        },
    )
    return clean_text(result)


@traceable(name="generate_subject_line")
def generate_subject(email_body: str) -> str:
    llm = get_llm(temperature=0.5)
    chain = subject_prompt | llm | parser

    result = chain.invoke(
        {"email_body": email_body},
        config={"tags": ["subject-generation"]},
    )
    return clean_text(result)


@traceable(name="generate_full_email")
def generate_full_email(
    purpose: str,
    recipient: str,
    key_points: str,
    tone: str = "professional",
    length: str = "medium (100-150 words)",
) -> dict:
    body = generate_email(purpose, recipient, key_points, tone, length)
    subject = generate_subject(body)
    return {"subject": subject, "body": body}