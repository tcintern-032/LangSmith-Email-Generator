import streamlit as st
from email_generator import generate_full_email
from utils import word_count

st.set_page_config(page_title="AI Email Generator", page_icon="✉️")

st.title("✉️ AI Email Generator")
st.caption("Built with LangChain + LangSmith tracing")

with st.form("email_form"):
    purpose = st.text_input(
        "Purpose", placeholder="e.g. Follow up after a job interview"
    )
    recipient = st.text_input(
        "Recipient", placeholder="e.g. Hiring manager, Sarah"
    )
    key_points = st.text_area(
        "Key points to include",
        placeholder="e.g. Thank them for their time, reiterate interest, ask about timeline",
    )
    tone = st.selectbox(
        "Tone",
        ["professional", "friendly", "formal", "casual", "persuasive"],
    )
    length = st.selectbox(
        "Length",
        ["short (under 75 words)", "medium (100-150 words)", "long (200+ words)"],
    )
    submitted = st.form_submit_button("Generate Email")

if submitted:
    try:
        with st.spinner("Generating..."):
            result = generate_full_email(
                purpose=purpose,
                recipient=recipient,
                key_points=key_points,
                tone=tone,
                length=length,
            )
        st.success("Email generated — check LangSmith for the full trace.")
        st.subheader("Subject")
        st.write(result["subject"])
        st.subheader("Body")
        st.write(result["body"])
        st.caption(f"{word_count(result['body'])} words")
    except ValueError as e:
        st.error(str(e))