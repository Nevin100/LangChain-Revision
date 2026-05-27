from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

# Load the dotenv file to access environment variables
load_dotenv()

# Initialize the HuggingFaceEmbeddings with the specified model
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Embed a query using the HuggingFaceEmbeddings instance
result = embeddings.embed_query("MySelf Nevin Bali")

# Display the resulting embedding
print(str(result))
