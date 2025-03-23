import streamlit as st
from dotenv import load_dotenv
import os
from langchain_cohere import CohereEmbeddings, ChatCohere
from langchain_pinecone import Pinecone as LangchainPinecone
from langchain.chains import RetrievalQA

load_dotenv()

embeddings = CohereEmbeddings(model="embed-english-v3.0", cohere_api_key=os.getenv("COHERE_API_KEY"))
vectorstore = LangchainPinecone.from_existing_index("medical-assistant", embeddings)

llm = ChatCohere(model="command", cohere_api_key=os.getenv("COHERE_API_KEY"))

qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever(search_type="similarity", search_kwargs={"k":5}),
    return_source_documents=True
)

st.title("🩺 MediQuery")

query = st.text_input("Ask your medical question:")

if st.button("Get Answer"):
    result = qa({"query": query})
    st.write(result["result"])

    st.subheader("Sources and Relevant Information:")
    for idx, doc in enumerate(result["source_documents"], start=1):
        st.markdown(f"**Document {idx}:**")
        st.write(doc.page_content)
        st.write("---")
