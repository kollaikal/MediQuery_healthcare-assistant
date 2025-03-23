from dotenv import load_dotenv
import os
from langchain_cohere import CohereEmbeddings
from langchain_pinecone import Pinecone as LangchainPinecone
from langchain.text_splitter import RecursiveCharacterTextSplitter
from pinecone import Pinecone
import requests

load_dotenv()

# Initialize Pinecone
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index_name = "medical-assistant"

# Fetch PubMed Data
def fetch_pubmed_data(query, num_results=10):
    pubmed_api_key = os.getenv("PUBMED_API_KEY")
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={query}&retmax={num_results}&retmode=json&api_key={pubmed_api_key}"
    response = requests.get(url).json()
    id_list = response['esearchresult']['idlist']
    papers = []
    for pmid in id_list:
        detail_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={pmid}&retmode=text&rettype=abstract&api_key={pubmed_api_key}"
        abstract_text = requests.get(detail_url).text
        papers.append(abstract_text)
    return papers

# Get PubMed abstracts
documents = fetch_pubmed_data("hypertension treatment", num_results=10)

# Text splitting for better retrieval
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_splitter.create_documents(documents)

# Cohere embeddings
embeddings = CohereEmbeddings(model="embed-english-v3.0", cohere_api_key=os.getenv("COHERE_API_KEY"))

# Embed into Pinecone
vectorstore = LangchainPinecone.from_documents(docs, embeddings, index_name=index_name)

print("✅ PubMed abstracts embedded successfully!")

