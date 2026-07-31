# LangSmith-Email-Generator
A Python application built with **LangChain**, **OpenAI**, and **LangSmith** that demonstrates how to trace, debug, and monitor AI workflows. This project generates professional emails using an OpenAI language model while automatically recording prompts, responses, and execution traces in the LangSmith dashboard.
## Features
* OpenAI LLM Integration
* LangChain Prompt Templates
* LangSmith Tracing
* AI Email Generation
* Prompt & Response Logging
* Modular Project Structure
* Easy Configuration with Environment Variables
## Technologies Used
* Python 3.11+
* LangChain
* LangChain OpenAI
* LangSmith
* OpenAI API
* python-dotenv
## Project Structure
```text
langsmith-email-generator/
│── .env.example
│── .gitignore
│── LICENSE
│── app.py
│── email_generator.py
│── llm.py
│── prompts.py
│── requirements.txt
└── utils.py
```
 ## Environment Variables

Create a `.env` file using `.env.example`.

```env
OPENAI_API_KEY=your_openai_api_key
LANGSMITH_API_KEY=your_langsmith_api_key
LANGSMITH_TRACING=true
LANGSMITH_PROJECT=LangSmith-Email-Generator
```
## Running the Project

```bash
python app.py
```

---
## Example
### Input

```text
Subject:
Leave Application

Purpose:
Request leave for two days because of illness.
```
### Output

```text
Subject: Leave Application

Dear Manager,

I hope you are doing well.

I am writing to request a leave of absence for two days due to illness. I am currently unwell and need some time to recover before returning to work.

Thank you for your understanding.

Sincerely,
Your Name
```

---
## LangSmith Integration
This project uses LangSmith to provide complete observability of AI workflows.
When tracing is enabled, LangSmith records:
* Prompt Templates
* User Inputs
* Model Responses
* Token Usage
* Execution Flow
* Latency
* Errors
* Chain Execution
Open the LangSmith dashboard after running the project to inspect each execution trace.

---
## Assignment Objectives Covered

* Introduction to LangSmith
* LangSmith Tracing
* Debugging AI Workflows
* Monitoring LLM Calls
* Prompt and Response Tracking
* LangChain Integration
* OpenAI Integration
## Future Improvements

* Multiple Email Templates
* Conversation Memory
* Prompt Versioning
* Batch Email Generation
* Web Interface with FastAPI
* Email Tone Selection
* Streaming Responses
* Evaluation with LangSmith Datasets

---

## Screenshots

Add screenshots of:

* Application Output
* LangSmith Trace Dashboard
* Prompt Execution Flow

---
## Requirements
Install dependencies using:

```bash
pip install -r requirements.txt
```

---
## License
This project is licensed under the MIT License.
## Author
**Muhammad Zeeshan**
