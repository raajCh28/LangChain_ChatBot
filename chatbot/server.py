from fastapi import FastAPI
from langserve import add_routes

from chatbot.chain import chain


# Step 1: Create the FastAPI application.
app = FastAPI(
    title="Simple LangChain Chatbot API",
    version="1.0.0",
)

# Step 2: Expose the LangChain chain through /chat endpoints.
add_routes(app, chain, path="/chat")


# Step 3: Run this file with:
# uvicorn chatbot.server:app --reload