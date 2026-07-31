import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

REQUIRED_VARS = ["OPENAI_API_KEY", "LANGCHAIN_API_KEY"]
missing = [v for v in REQUIRED_VARS if not os.getenv(v)]
if missing:
    raise EnvironmentError(
        f"Missing required environment variables: {missing}. "
        f"Copy .env.example to .env and fill in your keys."
    )

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ.setdefault("LANGCHAIN_PROJECT", "email-generator")


def get_llm(temperature: float = 0.7) -> ChatOpenAI:
    return ChatOpenAI(
        model=os.getenv("MODEL_NAME", "gpt-4o-mini"),
        temperature=temperature,
    )