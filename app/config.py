import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

SEARCH_ENDPOINT = os.getenv("AZURE_AI_SEARCH")
INDEX_NAME = "indexRAG1799"
SEARCH_KEY = 

API_KEY = os.getenv("AZURE_API_KEY")
TARGET_URI = os.getenv("AZURE_TARGET_UI")

model_name = "gpt-4.1-mini"
deployment = "gpt-4.1-mini"
api_version = "2024-12-01-preview"
emb_model = "text-embedding-ada-002"