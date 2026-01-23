from openai import AzureOpenAI
from azure.search.documents import SearchClient
import uuid
from azure.core.credentials import AzureKeyCredential
from app.config import *


client = AzureOpenAI(
    api_version="2024-12-01-preview",
    azure_endpoint=TARGET_URI,
    api_key=API_KEY,
)

search_client = SearchClient(
    endpoint = SEARCH_ENDPOINT,
    index_name = INDEX_NAME,
    credential = AzureKeyCredential(SEARCH_KEY)
)

def get_embedd(text: str):
    emb = client.embeddings.create(
        model = emb_model,
        input = text
    )
    return emb.data[0].embedding

def index_doc(text: str):
    embd = get_embedd(text)
    doc = {
        "id" : str(uuid.uuid4()),
        "content" : text,
        "embedding" : embd,
        "provider" : "rohit"
    }
    search_client.upload_documents([doc])