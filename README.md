# LangChain GenAI Revision

> A comprehensive educational repository demonstrating how to build production-ready generative AI applications using LangChain.

An educational repository designed to teach and showcase best practices for building generative AI workflows with LangChain. This project covers everything from basic LLM interactions to advanced retrieval-augmented generation (RAG) pipelines, demonstrating how to integrate multiple AI model providers, create sophisticated chains, and build intelligent document processing systems.

The repository is organized as a series of self-contained, numbered modules. Each module focuses on a specific concept, allowing you to study, run, and modify code independently.

## 🎯 What This Project Covers

- **Language Models**: Direct LLM calls with Groq, OpenAI, Anthropic, and Google Gemini
- **Chat Models**: Structured conversations using `SystemMessage` and `HumanMessage`
- **Local Models**: Running open-source Hugging Face models locally (distilgpt2, etc.)
- **Embeddings**: Semantic search and similarity matching with HuggingFace embeddings
- **Structured Outputs**: Type-safe outputs using Pydantic, TypedDict, and JSON schemas
- **Chains**: Simple, sequential, parallel, and conditional workflow patterns
- **Runnables**: Composable primitives for building complex workflows
- **Document Loading**: Ingesting text, PDFs, directories, and web content
- **Text Splitting**: Intelligent chunking of long documents (character, semantic, and recursive strategies)
- **Vector Stores**: Semantic storage and retrieval with ChromaDB and FAISS
- **Retrievers**: Advanced retrieval strategies (CCR, MMR, Multi-Query, Wikipedia integration)
- **RAG Pipelines**: Production-ready question-answering over documents
- **Tools & Agents**: Building custom tools and AI agents for task automation

## 📁 Project Structure

The repository uses a numbered folder structure for easy navigation:

### Core LLM & Chat Models

| Module | Path | Purpose |
| --- | --- | --- |
| **1** | `1)LLMS/` | Basic language model interactions with ChatGroq |
| **2** | `2)Chat_Models/` | Chat-based interactions with system and user messages |
| **3** | `3)LocalModels/` | Running open-source models locally via Hugging Face |
| **4** | `4)Embedding_models/` | Generating embeddings for semantic operations |

### Output Formatting & Structured Data

| Module | Path | Purpose |
| --- | --- | --- |
| **5** | `5)Structured_outputs/` | Type-safe outputs (Pydantic, TypedDict, JSON) |
| | `5)Structured_outputs/structured_outputs/` | Structured examples with validation |
| | `5)Structured_outputs/unstructured_outputs/` | Flexible output parsing |

### Workflow Composition

| Module | Path | Purpose |
| --- | --- | --- |
| **6** | `6)Chains/` | LangChain chains (simple, sequential, parallel, conditional) |
| **7** | `7)Runnables/` | Composable runnable primitives |

### Document & Data Processing

| Module | Path | Purpose |
| --- | --- | --- |
| **8** | `8)Document_Loaders/` | Load documents from various sources (PDF, text, web, directories) |
| **9** | `9)TextSplitters/` | Intelligent text chunking strategies |

### Advanced Retrieval & RAG

| Module | Path | Purpose |
| --- | --- | --- |
| **10** | `10)Vector_Stores/` | Vector database integration (ChromaDB, FAISS) |
| **11** | `11)Retrievers/` | Advanced retrieval methods (CCR, MMR, Multi-Query, Wikipedia) |
| **12** | `12)RAG-Pipeline/` | Complete RAG system with YouTube transcript analysis |
| **13** | `13)Tools/` | Built-in and custom tools for agent operations |

## 📖 Module Details

### 1) LLMs - Language Models
```
1)LLMS/llm.py
```
- Basic `ChatGroq` invocation
- Temperature control for randomness
- Simple prompt-response workflows

### 2) Chat Models - Conversational AI
```
2)Chat_Models/
├── chat_model.py           # ChatGroq with system/human messages
└── huggingface_chat_model.py  # ChatHuggingFace integration
```
- Structured conversations with roles
- System prompts for behavior control
- Hugging Face model integration

### 3) Local Models - On-Device AI
```
3)LocalModels/hugging_face.py
```
- Running models without API calls
- Memory-efficient inference
- Local pipeline setup

### 4) Embedding Models - Semantic Vectors
```
4)Embedding_models/huggingFace_embeddings.py
```
- Convert text to semantic vectors
- All-MiniLM-L6-v2 embeddings
- Similarity search foundation

### 5) Structured Outputs - Type Safety
```
5)Structured_outputs/
├── structured_outputs/
│   ├── json_schema.py       # JSON-based output schemas
│   ├── ps.py                # Pydantic schema
│   ├── pydantic_ex.py       # Pydantic model extraction
│   └── typed_Dict.py        # TypedDict examples
└── unstructured_outputs/
    └── output_parsers1.py   # StringOutputParser
```
- Guarantee output format
- Type validation with Pydantic
- Custom schema definition

### 6) Chains - Workflow Composition
```
6)Chains/
├── simple_chain/simple_chain.py           # Basic prompt→model→parse
├── sequential_chain/sequential_chain.py   # Multi-step workflows
├── parallel_chain/parallel_chain.py       # Concurrent operations
└── condtional_chain/conditional_chain.py  # Branching logic (math vs general)
```
- Chain multiple components
- Sequential and parallel execution
- Conditional routing

### 7) Runnables - Composable Primitives
```
7)Runnables/
├── part1/runnable1.py           # Basic runnable patterns
└── part2/
    ├── Runnable_Sequence.py     # Sequential composition
    └── Runnable_Parallel.py     # Parallel execution
```
- LCEL (LangChain Expression Language)
- Composable with `|` operator
- Async-first design

### 8) Document Loaders - Data Ingestion
```
8)Document_Loaders/
├── TextLoader/code.py       # Plain text files
├── PyPdfLoader/code.py      # PDF documents
├── DirectoryLoader/code.py  # Bulk file loading
└── WebBasedLoader/code.py   # Web page scraping
```
- Multiple document formats
- Metadata preservation
- Batch operations

### 9) Text Splitters - Chunking Strategies
```
9)TextSplitters/
├── CharacterTextSplitting.py      # Simple character-based split
├── TextStructuredSpliting.py      # Recursive splitting
├── DocumentStructuredtextSplitter.py # Document-aware splitting
└── SemanticTextSplitting.py       # Meaning-preserving chunking
```
- Preserve context boundaries
- Chunk size and overlap control
- Semantic splitting for better coherence

### 10) Vector Stores - Semantic Storage
```
10)Vector_Stores/chromaDB/code.py
```
- ChromaDB integration
- Document embedding and storage
- Semantic search queries

### 11) Retrievers - Advanced Retrieval
```
11)Retrievers/
├── CCR/code.py                    # Contextual Compression Retrieval
├── MMR/code.py                    # Maximal Marginal Relevance
├── MultiQueryRetriever/code.py    # Query expansion
├── VectorSearchRetriever/code.py  # Basic similarity search
└── WikipediaRetriever/code.py     # Wikipedia integration
```
- Multiple retrieval strategies
- Reduce hallucinations with compression
- Diverse result selection with MMR

### 12) RAG Pipeline - End-to-End System
```
12)RAG-Pipeline/code.py
```
- Complete question-answering system
- YouTube transcript processing
- Document indexing and retrieval
- Query answering with context

### 13) Tools - Agent Tools
```
13)Tools/
├── Built/code.py     # Built-in tools (DuckDuckGo search)
└── custom/code.py    # Custom tool definitions
```
- Search integration
- Data retrieval tools
- Custom agent tools

## 🚀 Installation

### Prerequisites
- Python 3.12 or higher
- pip or poetry

### Setup Steps

1. **Clone or extract the repository**
```bash
cd LangChain-GenAI-Revision
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

Or using poetry:
```bash
poetry install
```

4. **Set up environment variables**

Create a `.env` file in the project root with your API keys:
```bash
GROQ_API_KEY=your_groq_api_key
OPENAI_API_KEY=your_openai_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
GOOGLE_API_KEY=your_google_api_key
HUGGINGFACE_API_KEY=your_huggingface_api_key
```

## 💻 Quick Start

### Run the main entry point
```bash
python main.py
```

### Run individual modules
```bash
# Basic LLM call
python 1)LLMS/llm.py

# Chat model example
python 2)Chat_Models/chat_model.py

# Simple chain
python 6)Chains/simple_chain/simple_chain.py

# RAG pipeline
python 12)RAG-Pipeline/code.py
```

## 📚 Key Concepts

### LangChain Expression Language (LCEL)
The pipe operator (`|`) chains components together:
```python
chain = prompt | model | parser
result = chain.invoke({"input": "value"})
```

### Chains
- **Simple**: Prompt → Model → Parser
- **Sequential**: Output of one step feeds into the next
- **Parallel**: Multiple branches execute simultaneously
- **Conditional**: Routes to different paths based on logic

### Embeddings
Convert text to numerical vectors for semantic operations:
- Similarity search
- Semantic clustering
- Recommendation systems

### RAG (Retrieval-Augmented Generation)
Combines information retrieval with generation:
1. Index documents with embeddings
2. Retrieve relevant chunks for queries
3. Generate answers grounded in retrieved context

## 📋 Dependencies

### Core LangChain
- `langchain` - Core library
- `langchain-core` - Base abstractions
- `langchain-community` - Community integrations
- `langchain-text-splitters` - Text chunking
- `langchain_huggingface` - Hugging Face integration

### Model Providers
- `langchain-groq` - Groq API
- `langchain-openai` - OpenAI models
- `langchain-anthropic` - Claude models
- `langchain-google-genai` - Google Gemini

### ML & Data
- `transformers` - Hugging Face models
- `pydantic` - Data validation
- `numpy` - Numerical computing
- `scikit-learn` - ML utilities

### Vector & Retrieval
- `chromadb` - Vector database
- `faiss-cpu` - Similarity search
- `wikipedia` - Wikipedia retrieval
- `sentence-transformers` - Embeddings

### Utilities
- `python-dotenv` - Environment variables
- `youtube-transcript-api` - YouTube transcripts
- `tiktoken` - Token counting

## 🎓 Learning Path

1. Start with **Module 1-2**: Understanding LLMs and chat models
2. Progress to **Module 4**: Embeddings and semantic search
3. Learn **Module 6-7**: Building chains and runnables
4. Explore **Module 8-9**: Document loading and chunking
5. Master **Module 12**: Building complete RAG pipelines
6. Advanced **Module 11**: Fine-tuning retrieval strategies
7. Extend **Module 13**: Creating custom tools and agents

## 📖 Usage Examples

### Simple Query
```python
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()
llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0.7)
response = llm.invoke("What is the capital of India?")
print(response.content)
```

### Building a Chain
```python
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

prompt = PromptTemplate(
    template="Generate 5 facts about {topic}",
    input_variables=["topic"]
)
model = ChatGroq(model="llama-3.1-8b-instant", temperature=0.3)
parser = StrOutputParser()

chain = prompt | model | parser
result = chain.invoke({"topic": "space exploration"})
```

### Using Embeddings
```python
from langchain_community.embeddings import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
text_embedding = embeddings.embed_query("Hello world")
```

## 🤝 Contributing

This is an educational repository. Feel free to:
- Modify examples to test your understanding
- Add new examples for additional concepts
- Fix bugs or improve documentation
- Experiment with different models and parameters

## 📝 Notes

- Each module is self-contained and can run independently
- Examples use environment variables for API keys (create a `.env` file)
- Some modules require specific API keys (Groq, OpenAI, etc.)
- Local models can be used without API keys but require more computational resources
- The RAG pipeline demonstrates production-ready patterns for Q&A systems

## 🔗 Resources

- [LangChain Documentation](https://python.langchain.com/)
- [Groq API](https://console.groq.com/)
- [Hugging Face Models](https://huggingface.co/models)
- [ChromaDB Documentation](https://docs.trychroma.com/)
- [OpenAI API](https://platform.openai.com/)

## ⚠️ Prerequisites & Notes

### System Requirements
- Python 3.12 or higher
- Virtual environment strongly recommended
- Internet access for hosted models and external services
- 4GB+ RAM for local models (more for larger models)

### Important Notes
- The numbered folders keep examples organized by topic and learning progression
- Most scripts are intentionally educational rather than production-ready
- Examples depend on community packages: `langchain-community`, `langchain-huggingface`, `langchain-text-splitters`
- Document loader and splitter examples provide a foundation for RAG pipelines
- Some features require specific API keys (see `.env` setup above)
- Local models don't require API keys but need more computational resources
- You only need API keys for the providers you actually use

### Recommended Learning Order
1. Start with Modules 1-2 (LLMs and Chat)
2. Try local models (Module 3) to understand the differences
3. Learn embeddings (Module 4) for semantic operations
4. Build chains (Modules 6-7) for workflow composition
5. Practice document processing (Modules 8-9)
6. Master RAG (Module 12) for production patterns
7. Explore advanced retrieval (Module 11)
8. Create custom tools (Module 13)

## 📞 Troubleshooting

**API Key Issues**: Make sure your `.env` file is in the project root and uses correct variable names.

**Module Not Found**: Install missing dependencies with `pip install -r requirements.txt`

**Import Errors**: Ensure virtual environment is activated and dependencies are installed.

**Model Download Issues**: Some Hugging Face models auto-download on first run. Ensure stable internet connection.

---

*This repository is designed as an educational resource for learning LangChain. Contributions and modifications are encouraged to deepen your understanding.*
