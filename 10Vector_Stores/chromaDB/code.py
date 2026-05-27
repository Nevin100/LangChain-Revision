from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_community.embeddings import HuggingFaceEmbeddings
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Embedding model
embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Documents
docs = [
    Document(page_content="This is the first document.", metadata={"source": "doc1"}),
    Document(page_content="This is the second document.", metadata={"source": "doc2"}),
    Document(page_content="This is the third document.", metadata={"source": "doc3"}),
]

# Create vector storex``
vector_store = Chroma.from_documents(
    documents=docs,
    embedding=embedding,
    collection_name="my_collection"
)

# Add new document
new_doc = Document(page_content="This is the fourth document.", metadata={"source": "doc4"})
vector_store.add_documents([new_doc])

# View stored docs
all_docs = vector_store.get()
print(all_docs)

# Similarity search
query = "second document"
results = vector_store.similarity_search(query, k=2)

for doc in results:
    print(doc.page_content, doc.metadata)

# Metadata filtering
filtered = vector_store.similarity_search(
    query,
    k=2,
    filter={"source": "doc2"}
)

for doc in filtered:
    print("Filtered:", doc.page_content)