# Document Loader in RAG:
# The Document Loader is a crucial component in the Retrieval-Augmented Generation (RAG) framework. It is responsible for loading and preprocessing documents that will be used for retrieval during the generation process. The Document Loader typically performs tasks such as reading documents from various sources (e.g., files, databases, APIs), cleaning and normalizing the text, and converting it into a format suitable for indexing and retrieval.
# Structure of Document : page_content and metadata


# 1. TextLoader:
# It is a specific implementation of a Document Loader that focuses on loading and processing text documents. The TextLoader can handle various text formats, such as plain text files, PDFs, or even web pages. It may include functionalities like tokenization, stop word removal, and stemming to prepare the text for efficient retrieval.Only works with txt files.

from langchain_community.document_loaders import TextLoader

# Create an instance of the TextLoader, specifying the path to the text file you want to load. In this example, we are loading a file named "example.txt". Make sure that the file exists in the specified location and contains the text data you want to use for retrieval.
loader = TextLoader("example.txt")

# Load the documents from the specified file. The loader will read the contents of "example.txt", preprocess it according to its internal logic, and return a list of document objects that can be used for retrieval in the RAG framework.
docs = loader.load()

# Finally, we print the loaded documents to verify that they have been successfully loaded and preprocessed. The output will depend on the contents of "example.txt" and how the TextLoader processes it, but it should display the text data in a structured format suitable for retrieval.Importantly, the type of output is List of Document objects, which can be used in subsequent steps of the RAG pipeline for indexing and retrieval.
print(docs)