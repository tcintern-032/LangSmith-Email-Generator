from langchain_core.prompts import ChatPromptTemplate

EMAIL_SYSTEM_PROMPT = """You are an expert copywriter who writes clear,
professional emails. Match the requested tone exactly, keep the email
focused, and never pad it with filler. Do not include a subject line
unless explicitly asked to."""

email_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", EMAIL_SYSTEM_PROMPT),
        (
            "user",
            "Write an email with the following details:\n"
            "Purpose: {purpose}\n"
            "Recipient: {recipient}\n"
            "Tone: {tone}\n"
            "Key points to include: {key_points}\n"
            "Approximate length: {length}",
        ),
    ]
)

SUBJECT_SYSTEM_PROMPT = """You write short, high-open-rate email subject
lines. Return only the subject line text, nothing else — no quotes,
no labels."""

subject_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", SUBJECT_SYSTEM_PROMPT),
        ("user", "Email body:\n{email_body}\n\nWrite one subject line for it."),
    ]
)