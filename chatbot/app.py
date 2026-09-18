import json
from urllib.request import Request, urlopen

import streamlit as st


# Step 1: Point Streamlit to the running FastAPI endpoint.
API_URL = "http://127.0.0.1:8000/chat/invoke"

# Step 2: Create the simple Streamlit input.

st.title("LangChain ChatBot")
input_text = st.text_input("Enter your query:")


# Step 3: Send the question to LangServe when the user enters one.
def ask_api(question):
    request_body = {"input": {"input": question}}
    request = Request(
        API_URL,
        data=json.dumps(request_body).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    with urlopen(request) as response:
        result = json.loads(response.read().decode("utf-8"))

    return result["output"]

if input_text:
    response = ask_api(input_text)
    st.write("Response:", response)