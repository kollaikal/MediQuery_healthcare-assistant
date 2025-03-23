from dotenv import load_dotenv
import os
from langchain_cohere import CohereEmbeddings
from langchain_pinecone import Pinecone as LangchainPinecone
from langchain.text_splitter import RecursiveCharacterTextSplitter
from pinecone import Pinecone, ServerlessSpec

load_dotenv()

# Pinecone initialization
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index_name = "medical-assistant"

if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=1024,  # Cohere embeddings dimension is 1024
        metric='cosine',
        spec=ServerlessSpec(cloud='aws', region='us-east-1')
    )

# Documents to embed
documents = [
    "Hypertension is treated using ACE inhibitors.",
    "Beta-blockers are medications for cardiovascular diseases."
]

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_splitter.create_documents(documents)

# Cohere embeddings
embeddings = CohereEmbeddings(model="embed-english-v3.0", cohere_api_key=os.getenv("COHERE_API_KEY"))

# Load embeddings into Pinecone
vectorstore = LangchainPinecone.from_documents(docs, embeddings, index_name=index_name)

print("✅ Cohere embeddings loaded successfully into Pinecone!")
