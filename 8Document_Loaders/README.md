# 📖 Folder 8: Document Loaders

## 🎯 Objective

Load documents from multiple sources (Text, PDF, Web, Directories) and convert them into LangChain Document objects. First step of document processing pipeline.

## 📚 Theory & Concepts

### **LangChain Document Object**

```python
class Document:
    page_content: str           # Actual text
    metadata: Dict[str, Any]    # Source info, page number, etc.

Example:
Document(
    page_content="Python is a programming language...",
    metadata={"source": "guide.pdf", "page": 1}
)
```

### **Loader Pattern**

```
File/Source → Loader → Document Objects → Processing Pipeline
                                    ↓
                            Vector Stores
                                    ↓
                            Retrieval Systems
```

### **Document vs Text**

```
Raw Text File:
"This is content\nMore content\n..."

LangChain Document:
{
    "page_content": "This is content\nMore content\n...",
    "metadata": {"source": "file.txt", "encoding": "utf-8"}
}

Advantage: Trackable source, structured format, queryable metadata
```

### **Loader Types in This Folder**

```
1. TextLoader
   └── Simple .txt files → Document

2. PyPdfLoader
   └── PDF files → Document per page

3. DirectoryLoader
   └── Multiple files directory → Documents list

4. WebBasedLoader
   └── URLs → Document from webpage
```

### **Metadata - Why Important**

```
Vector Store + Metadata:
├── Can filter by source
├── Track document origin
├── Include page numbers
├── Store custom fields
└── Later: "Show me results from page 5"

Without metadata:
├── Can't trace results
├── Don't know where info came from
└── Less useful for production
```

## 📁 Files Overview

### **TextLoader/**
```
Purpose: Load single or multiple .txt files
Method: TextLoader class
Output: List of Documents
```

### **PyPdfLoader/**
```
Purpose: Extract text from PDF files
Method: PyPdfLoader class
Output: One Document per page with page_number metadata
Note: Text-based PDFs only (not OCR for images)
```

### **DirectoryLoader/**
```
Purpose: Batch load all files from directory
Method: DirectoryLoader with pattern
Output: Documents from all matching files
Useful: Loading all docs at once
```

### **WebBasedLoader/**
```
Purpose: Fetch content from URLs
Method: WebBaseLoader (uses BeautifulSoup)
Output: Document with webpage text
Limitation: No JavaScript rendering
```

## 🔑 Key Learning Points

### **1. TextLoader - Single File**

```python
from langchain_community.document_loaders import TextLoader

loader = TextLoader("path/to/file.txt")
documents = loader.load()

# documents = [Document(
#     page_content="File content here...",
#     metadata={"source": "path/to/file.txt"}
# )]

print(documents[0].page_content)
print(documents[0].metadata)
```

### **2. PyPdfLoader - PDF Files**

```python
from langchain_community.document_loaders import PyPdfLoader

loader = PyPdfLoader("document.pdf")
documents = loader.load()

# Each page = separate Document!
print(f"Total pages: {len(documents)}")

for doc in documents:
    print(f"Page {doc.metadata['page']}: {doc.page_content[:100]}")
```

### **3. DirectoryLoader - Multiple Files**

```python
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import TextLoader

loader = DirectoryLoader(
    "./documents",              # Directory path
    glob="**/*.txt",           # File pattern (all .txt files)
    loader_cls=TextLoader       # Which loader to use
)

documents = loader.load()
print(f"Loaded {len(documents)} documents")
```

### **4. WebBaseLoader - Web Content**

```python
from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://example.com/article")
documents = loader.load()

print(documents[0].page_content)  # Article text
print(documents[0].metadata)      # {"source": "https://example.com/..."}
```

### **5. Batch Loading Multiple URLs**

```python
from langchain_community.document_loaders import WebBaseLoader

urls = [
    "https://example.com/page1",
    "https://example.com/page2",
    "https://example.com/page3",
]

loaders = [WebBaseLoader(url) for url in urls]
documents = []

for loader in loaders:
    try:
        documents.extend(loader.load())
    except Exception as e:
        print(f"Error loading {loader}: {e}")
```

## 💡 Practical Patterns

### **Pattern 1: Load Everything from Directory**

```python
from pathlib import Path
from langchain_community.document_loaders import DirectoryLoader, TextLoader

# Load all text files
documents = DirectoryLoader(
    "./data",
    glob="**/*.txt",
    loader_cls=TextLoader
).load()

# Load all PDFs
from langchain_community.document_loaders import PyPdfLoader

pdf_documents = DirectoryLoader(
    "./data",
    glob="**/*.pdf",
    loader_cls=PyPdfLoader
).load()

all_documents = documents + pdf_documents
print(f"Total: {len(all_documents)} documents")
```

### **Pattern 2: Add Custom Metadata**

```python
from langchain_community.document_loaders import TextLoader
from datetime import datetime

def load_with_metadata(file_path, category):
    loader = TextLoader(file_path)
    documents = loader.load()
    
    for doc in documents:
        doc.metadata["category"] = category
        doc.metadata["loaded_at"] = datetime.now().isoformat()
    
    return documents

# Usage
docs = load_with_metadata("guide.txt", "tutorial")
# metadata now has: source, category, loaded_at
```

### **Pattern 3: Filter During Loading**

```python
from langchain_community.document_loaders import DirectoryLoader

loader = DirectoryLoader(
    "./documents",
    glob="**/*.txt"
)

all_docs = loader.load()

# Filter by size
large_docs = [d for d in all_docs if len(d.page_content) > 1000]
small_docs = [d for d in all_docs if len(d.page_content) <= 1000]
```

### **Pattern 4: Error Handling**

```python
from langchain_community.document_loaders import WebBaseLoader
import logging

logging.basicConfig(level=logging.INFO)

urls = ["valid_url", "invalid_url", "another_url"]
documents = []

for url in urls:
    try:
        loader = WebBaseLoader(url)
        docs = loader.load()
        documents.extend(docs)
        logging.info(f"✅ Loaded: {url}")
    except Exception as e:
        logging.error(f"❌ Failed {url}: {e}")
```

## 📊 Loader Comparison

| Loader | Source | Speed | Output | Metadata |
|--------|--------|-------|--------|----------|
| TextLoader | .txt | ⚡⚡⚡ | 1 Document | filename |
| PyPdfLoader | .pdf | ⚡⚡ | N Documents | page number |
| DirectoryLoader | Directory | ⚡⚡ | N Documents | filename |
| WebBaseLoader | URL | ⚡ | 1 Document | URL |

## 🎓 Advanced Concepts

### **Streaming Large Files**

```python
# Don't load entire file if too large
def stream_large_file(file_path, chunk_size=1000):
    with open(file_path, 'r') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            yield Document(
                page_content=chunk,
                metadata={"source": file_path}
            )
```

### **PDF Extraction Limitations**

```
PDF Types:
1. Text-based PDF ✅
   └── PyPdfLoader can extract text directly

2. Scanned PDF (Image) ❌
   └── PyPdfLoader won't work
   └── Need OCR (Tesseract, etc.)

3. Encrypted PDF ❌
   └── Need password or decryption
```

### **Web Loading Limitations**

```
WebBaseLoader uses:
├── BeautifulSoup (HTML parsing)
├── No JavaScript execution
└── Static content only

Cannot load:
├── Dynamic content (JavaScript-heavy)
├── Behind login
├── Protected content
```

## 🛠️ Setup Requirements

### **PDF Support**

```bash
# Already included in requirements.txt
pip install pypdf
```

### **Web Loading Support**

```bash
# Already included
pip install beautifulsoup4
```

## 📝 Metadata Best Practices

```python
# Good metadata
Document(
    page_content="...",
    metadata={
        "source": "document.pdf",
        "page": 5,
        "category": "tutorial",
        "author": "John",
        "date": "2024-01-01"
    }
)

# Benefits:
├── Filtering: Get docs from specific author
├── Grouping: Group by category
├── Tracking: Know where results came from
└── Ranking: Newer docs might be preferred
```

## ⚠️ Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| FileNotFoundError | Check file path, use absolute paths |
| PDF corrupted | Try different PDF or OCR |
| Web timeout | Increase timeout, try different URL |
| Memory issues | Don't load all at once, stream instead |

## 💡 Pro Tips

1. **Metadata**: Always add meaningful metadata
2. **Batch**: Use DirectoryLoader for multiple files
3. **Error Handling**: Always wrap in try-except
4. **Validation**: Check document.page_content not empty
5. **Caching**: Cache loaded documents to avoid re-loading

## 📚 Common Document Patterns

### **Load & Split**
```python
documents = loader.load()
# Next step: TextSplitter (Folder 9)
```

### **Load & Embed**
```python
documents = loader.load()
# Next step: Create embeddings (Folder 4)
# Then: Vector store (Folder 10)
```

### **Load & Index**
```python
documents = loader.load()
# Full pipeline to RAG (Folder 12)
```

## 🔗 Document Processing Pipeline

```
Loaders (Folder 8)
    ↓ Load documents
Text Splitters (Folder 9)
    ↓ Chunk into pieces
Embeddings (Folder 4)
    ↓ Convert to vectors
Vector Stores (Folder 10)
    ↓ Store for retrieval
Retrievers (Folder 11)
    ↓ Search efficiently
RAG Pipeline (Folder 12)
    ↓ Generate answers
```

## 🚀 Next Steps

1. **Folder 9**: Split documents into chunks
2. **Folder 10**: Store in vector database
3. **Folder 11**: Retrieve for Q&A
4. **Folder 12**: Complete RAG system

---

**Document Loading Mastered! 📚**