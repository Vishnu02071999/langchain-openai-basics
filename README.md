# langchain-openai-basics

This project demonstrates how to use LangChain with OpenAI's Language Models to generate responses from natural language prompts.

In this example, we:

Load environment variables from a .env file.
Initialize an OpenAI LLM using LangChain.
Send a prompt to the model.
Print the generated response.

# Code

from langchain_openai import OpenAI
from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv()

llm = OpenAI(model="gpt-3.5-turbo-instruct")

result = llm.invoke("What is the capital of India?")

print(result)


📖 Explanation
1. Import Required Libraries
from langchain_openai import OpenAI
from dotenv import load_dotenv
langchain_openai: Provides integration between LangChain and OpenAI models.
python-dotenv: Loads environment variables from a .env file.
2. Load Environment Variables
load_dotenv()

This function loads variables from the .env file into the application's environment.

Example .env file:

OPENAI_API_KEY=your_api_key_here

This keeps sensitive information such as API keys secure and prevents them from being hardcoded into the source code.

3. Initialize the Language Model
llm = OpenAI(model="gpt-3.5-turbo-instruct")

This creates an instance of the OpenAI model.

gpt-3.5-turbo-instruct is an instruction-following model.
The model uses the API key loaded from the environment variables.
4. Invoke the Model
result = llm.invoke("What is the capital of India?")

The prompt is sent to the language model, which processes it and generates a response.

Expected Output:

New Delhi
5. Print the Result
print(result)

Displays the model's response in the terminal.



Install Dependencies
pip install langchain-openai python-dotenv
🔑 Configure OpenAI API Key

Create a .env file in the project root directory:

OPENAI_API_KEY=your_api_key_here

Replace your_api_key_here with your actual OpenAI API key.

▶️ Run the Application
python app.py
Sample Output
New Delhi

🧠 What I Learned
How to securely manage API keys using .env files.
How to integrate OpenAI models with LangChain.
How to send prompts to an LLM using invoke().
Basic LangChain workflow for interacting with language models.

📚 Technologies Used
Python
LangChain
OpenAI API
Python Dotenv
