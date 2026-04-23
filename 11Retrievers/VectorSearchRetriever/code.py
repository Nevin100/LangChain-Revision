# Vector Store Retriever 
# It is a retriever that uses a vector store to retrieve relevant documents based on their vector representations.
# The retriever takes a query, converts it into a vector representation, and then searches the vector store for the most similar vectors, which correspond to the relevant documents.

from  langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings

# Create sample documents with metadata
documents = [
    Document(page_content="This is the first document.", metadata={"source": "doc1.txt"}),
    Document(page_content="This is the second document.", metadata={"source": "doc2.txt"})
]

# Initialize the HuggingFaceEmbeddings with the specified model 
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Create a Chroma vector store from the documents and their embeddings
vector_store = Chroma.from_documents(documents=documents, embedding=embeddings)

# Create a retriever from the vector store with search parameters
retriever = vector_store.as_retriever(search_kwargs={"k": 1})

# Define a query to retrieve relevant documents
query = "What is the content of the first document?"

# Invoke the retriever with the query to get relevant documents
results = retriever.invoke(query)

# Display the retrieved results with their content and source metadata
for i, doc in enumerate(results):
    print(f"Result {i+1}: {doc.page_content} (Source: {doc.metadata['source']})")