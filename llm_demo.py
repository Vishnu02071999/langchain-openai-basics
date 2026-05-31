from langchain_openai import OpenAI
from dotenv import load_dotenv # helps in loading secret key from env file
import os
from pathlib import Path

load_dotenv() # this will load the environment variables from the .env file in the current directory.


llm=OpenAI(model="gpt-3.5-turbo-instruct") # you can specify the model you want to use here, by default it will use gpt-3.5-turbo-instruct which is a powerful model for instruction following tasks.

result=llm.invoke("What is the capital of India?") # this will return a response from the model, you can pass a prompt to it as well.

print(result)