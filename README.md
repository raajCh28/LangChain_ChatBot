# LangChain ChatBot

A simple chatbot built with LangChain, OpenAI, FastAPI, LangServe, and Streamlit.

## Features

- OpenAI-powered conversational responses
- LangChain prompt and output parsing pipeline
- FastAPI endpoint exposed through LangServe
- Streamlit web interface
- Optional LangSmith tracing

## Project Structure

```text
.
|-- chatbot/
|   |-- app.py       # Streamlit user interface
|   |-- chain.py     # LangChain prompt and model chain
|   `-- server.py    # FastAPI and LangServe API
|-- requirements.txt
|-- .gitignore
`-- README.md
```

## Requirements

- Python 3.10 or newer
- An OpenAI API key
- Optional: a LangSmith API key for tracing

## Setup

1. Clone the repository:

   ```powershell
   git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
   cd YOUR_REPOSITORY
   ```

2. Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Install the dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root:

   ```env
   OPENAI_API_KEY=your_openai_api_key
   LANGCHAIN_API_KEY=your_langsmith_api_key
   ```

   `LANGCHAIN_API_KEY` is optional. The `.env` file is ignored by Git and must never be committed.

## Run the Application

Start the API server from the project root:

```powershell
uvicorn chatbot.server:app --reload
```

In a second terminal, activate the virtual environment and start Streamlit:

```powershell
.\.venv\Scripts\Activate.ps1
streamlit run chatbot/app.py
```

Open the Streamlit URL shown in the terminal, usually:

```text
http://localhost:8501
```

The API is available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

## API Endpoint

The chatbot chain is exposed through LangServe at:

```text
POST /chat/invoke
```

Example request body:

```json
{
  "input": {
    "input": "What is LangChain?"
  }
}
```

## Security

- Do not commit `.env` or API keys.
- Do not put secret keys directly in Python source files.
- If a key is accidentally exposed, revoke it and create a new one immediately.

## License

No license has been specified for this project yet.
