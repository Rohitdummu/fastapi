from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
from app.config import *


search_client = SearchClient(
    endpoint = SEARCH_ENDPOINT,
    index_name = INDEX_NAME,
    credential = AzureKeyCredential(SEARCH_KEY)
)

def retriver(query: str, top_k=5):
    res = search_client.search(query, top_k=5)
    docs = [r["content"] for r in res]
    return docs