# 3. Directory Loader :
# The Directory Loader is a powerful tool that allows you to load multiple documents from a specified directory. It can be used to efficiently process and analyze large collections of documents, making it ideal for tasks such as data analysis, machine learning, and natural language processing. The Directory Loader can be configured to load various types of documents, including text files, PDFs, and more. It provides options for filtering files based on extensions, handling subdirectories, and managing memory usage during the loading process. This makes it a versatile solution for working with large datasets and streamlining your document processing workflow.

from langchain_community.document_loaders import DirectoryLoader, TextLoader

# Create a DirectoryLoader instance, specifying the path to the directory and the file type to load
loader = DirectoryLoader("path/to/directory", glob="**/*.txt", loader_cls=TextLoader)

# Load the documents from the specified directory
docs = loader.load()

# Print the loaded documents
print(docs)