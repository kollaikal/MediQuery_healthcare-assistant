from dotenv import load_dotenv
import os
from pinecone import Pinecone
from langchain_pinecone import Pinecone as LangchainPinecone
from langchain_cohere import CohereEmbeddings

load_dotenv()

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index_name = "medical-assistant"

embeddings = CohereEmbeddings(model="embed-english-v3.0", cohere_api_key=os.getenv("COHERE_API_KEY"))
vectorstore = LangchainPinecone.from_existing_index(index_name, embeddings)

query = "Recent hypertension treatments from PubMed"
docs = vectorstore.similarity_search(query, k=3)

print("✅ Top matching documents:")
for doc in docs:
    print("\n---\n")
    print(doc.page_content)
