import os
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec

# Load environment variables
load_dotenv()

# Initialize Pinecone client
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

# Define index name and settings
index_name = "medical-assistant"

# Check if index exists, else create one
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=1536,
        metric="cosine",  # Change to "euclidean" or "dotproduct" if needed
        spec=ServerlessSpec(
            cloud="aws",  # Change to your cloud provider if different
            region=os.getenv("PINECONE_ENVIRONMENT")  # Example: "us-west-2"
        )
    )
    print(f"Created index: {index_name}")
else:
    print(f"Index '{index_name}' already exists.")
