# Retrievers in Langchain:
# retievers are used to retrieve relevant documents from a knowledge base or database based on a query. They are an essential component of many natural language processing (NLP) applications, such as question answering systems, chatbots, and information retrieval systems.
# Retrievers typically work by taking a user's query and searching through a collection of documents to find those that are most relevant to the query. They may use various techniques, such as keyword matching, semantic similarity, or machine learning models, to determine the relevance of documents to the query.

# 1. WikipediaRetriever:
# The WikipediaRetriever is a specific type of retriever that is designed to retrieve relevant information from Wikipedia articles. It can be used to answer questions or provide information based on the content of Wikipedia pages. The WikipediaRetriever may utilize techniques such as keyword matching, semantic analysis, or machine learning models to identify and retrieve relevant sections of Wikipedia articles that pertain to the user's query.

from langchain_community.retrievers import WikipediaRetriever

# Example usage of WikipediaRetriever
retriever = WikipediaRetriever(
    top_k_results=5, # Number of relevant documents to retrieve 
    language="en" # Language of the Wikipedia articles to search (e.g., "en" for English)
)

# Query to retrieve relevant documents from Wikipedia
query = "What is the capital of France?"

# Retrieve relevant documents based on the query
results = retriever.invoke(query)

# Print the retrieved results
for i, result in enumerate(results):
    print(f"Result {i + 1}:")
    print(f"Title: {result.metadata['title']}")
    print(f"Content: {result.page_content}") 
    print("\n")