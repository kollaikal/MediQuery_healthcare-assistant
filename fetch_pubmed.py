import requests
from dotenv import load_dotenv
import os

load_dotenv()
pubmed_api_key = os.getenv("PUBMED_API_KEY")

def fetch_pubmed_data(query, num_results=10):
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={query}&retmax={num_results}&retmode=json&api_key={pubmed_api_key}"
    response = requests.get(url).json()
    id_list = response['esearchresult']['idlist']

    papers = []
    for pmid in id_list:
        detail_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={pmid}&retmode=text&rettype=abstract&api_key={pubmed_api_key}"
        abstract_text = requests.get(detail_url).text
        papers.append({"pmid": pmid, "abstract": abstract_text})
    return papers

if __name__ == "__main__":
    papers = fetch_pubmed_data("hypertension treatment", num_results=5)
    for paper in papers:
        print(paper["abstract"])

