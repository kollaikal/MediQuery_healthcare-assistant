# MediQuery Healthcare Assistant 🩺

## Overview
MediQuery is an AI-powered Healthcare Assistant that leverages advanced NLP techniques, vector embeddings (Cohere AI), and Pinecone's vector database for real-time retrieval of medical information from trusted resources such as PubMed. The assistant provides accurate, evidence-based answers to medical queries, symptom analysis, and healthcare guidance.

## Project Structure

```
MediQuery_healthcare-assistant/
├── app.py                    # Streamlit Web Interface
├── embed_documents.py        # Embeds general medical documents into Pinecone
├── embed_pubmed.py           # Fetches and embeds abstracts from PubMed
├── fetch_pubmed.py           # Retrieves medical abstracts using PubMed API
├── pinecone_setup.py         # Initializes Pinecone vector database
├── verify_embeddings.py      # Verifies embeddings stored in Pinecone
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
├── .gitignore                # Specifies files to ignore in Git
└── .env.example              # Template for environment variables
```

## Key Features
- Real-time semantic search and retrieval
- Integration of latest medical research via PubMed API
- User-friendly conversational interface using Streamlit
- Secure and scalable storage using Pinecone
- Cohere AI embeddings for accurate semantic representation

## Technologies Used
- **Python**: Primary programming language
- **Streamlit**: Web application interface
- **Cohere AI**: NLP embeddings and language generation
- **Pinecone**: Vector database
- **PubMed API**: Real-time medical research data retrieval

## Quick Setup

### Step 1: Clone Repository
```bash
git clone https://github.com/kollaikal/MediQuery_healthcare-assistant.git
cd MediQuery_healthcare-assistant
```

### Step 2: Setup Python Environment
```bash
python3 -m venv ai-env
source ai-env/bin/activate
pip install -r requirements.txt
```

### Step 3: Set Up Environment Variables
- nano `.env`
- Fill in your API keys:
```env
COHERE_API_KEY=your-cohere-api-key
PINECONE_API_KEY=your-pinecone-api-key
PINECONE_ENVIRONMENT=your-pinecone-environment
PUBMED_API_KEY=your-pubmed-api-key
```

### Step 4: Initialize and Embed Data
```bash
python pinecone_setup.py
python embed_documents.py
python embed_pubmed.py
```

### Step 5: Run Web Application
```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501`

## Usage
Type any medical-related question, and MediQuery will provide detailed answers sourced from PubMed and other medical databases.

Example Queries:
- "What treatments are currently recommended for hypertension?"
- "Explain the side effects of beta-blockers."

## Contributing
Feel free to contribute! Open issues or submit pull requests for enhancements or bug fixes.

## License
This project is open-sourced under the MIT License.

