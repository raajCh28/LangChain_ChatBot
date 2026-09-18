import os

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


# Step 1: Load the keys from the existing .env file.
load_dotenv()

# Step 2: Enable LangSmith tracing when the existing key is available.
if os.getenv("LANGCHAIN_API_KEY"):
    os.environ["LANGCHAIN_TRACING_V2"] = "true"

# Step 3: Create the prompt that receives the API input.
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful assistant. Please provide concise and accurate responses to user queries.",
    ),
    ("user", "input: {input}"),
])

# Step 4: Create the model and connect all steps into one chain.
llm = ChatOpenAI(model="gpt-4o")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser