# Multi Query Retriever (MQR) is a method that enhances the retrieval process by generating multiple queries from a single input query. This approach allows for a more comprehensive search of the document space, potentially retrieving more relevant and diverse results. The MQR process typically involves using a language model to generate variations of the original query, which are then used to retrieve documents from a vector store. The retrieved documents can be aggregated and ranked based on relevance to the original query, providing a richer set of results for downstream applications.

from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_groq import ChatGroq
from langchain_community.retrievers import MultiQueryRetriever

# Documents
docs = [
    Document(page_content="Langchain is a framework for building LLM applications.", metadata={"source": "doc1"}),
    Document(page_content="Langchain enables chaining of components for LLM workflows.", metadata={"source": "doc2"}),
    Document(page_content="MMR improves diversity in document retrieval.", metadata={"source": "doc3"}),
]

# Embeddings + Vector Store
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_store = Chroma.from_documents(docs, embeddings)

# Base retriever (MMR for diversity, optional)
base_retriever = vector_store.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 2,
        "fetch_k": 5,
        "lambda_mult": 0.5
    }
)

# LLM
llm = ChatGroq(model="llama3-70b-versatile", temperature=0)

# Multi Query Retriever — correct way
multi_query_retriever = MultiQueryRetriever.from_llm(
    retriever=base_retriever,
    llm=llm
)

# Query
query = "What is Langchain?"
results = multi_query_retriever.invoke(query)

for i, doc in enumerate(results):
    print(f"{i+1}: {doc.page_content}")