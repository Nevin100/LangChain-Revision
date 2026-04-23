# Maximal Marginal relevance (MMR) is a method used in information retrieval to select a subset of documents that are both relevant to a query and diverse from each other. The MMR algorithm works by iteratively selecting documents that maximize the relevance to the query while minimizing the redundancy with already selected documents.

from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# Documents
docs = [
    Document(page_content="Langchain is a powerful framework for building applications with language models.", metadata={"source": "doc1.txt"}),
    Document(page_content="Langchain with MMR is a method for selecting relevant and diverse documents in information retrieval.", metadata={"source": "doc2.txt"}),
    Document(page_content="Langchain consists of various components for building language model applications.", metadata={"source": "doc3.txt"})
]

# Embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Vector store
vector_store = Chroma.from_documents(docs, embeddings)

# MMR Retriever
retriever = vector_store.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 2,          # final results
        "fetch_k": 5,    # candidates before MMR filtering
        "lambda_mult": 0.5  # balance relevance vs diversity
    }
)

# Query
query = "What is Langchain?"

# Results 
results = retriever.invoke(query)

for i, doc in enumerate(results):
    print(f"Result {i+1}: {doc.page_content} (Source: {doc.metadata['source']})")