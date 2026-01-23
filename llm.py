import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("AZURE_API_KEY")
TARGET_URI = os.getenv("AZURE_TARGET_UI")

model_name = "gpt-4.1-mini"
deployment = "gpt-4.1-mini"
api_version = "2024-12-01-preview"

client = AzureOpenAI(
    api_version="2024-12-01-preview",
    azure_endpoint=TARGET_URI,
    api_key=API_KEY,
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "I am going to Paris, what should I see?",
        }
    ],
    max_completion_tokens=13107,
    temperature=1.0,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    model=deployment,
    stream=True,
)

for update in response:
    if update.choices:
        print(update.choices[0].delta.content or "", end="")

client.close()