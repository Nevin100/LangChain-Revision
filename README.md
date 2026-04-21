# LangChain GenAI Revision

An educational LangChain playground that demonstrates how to build generative AI workflows with multiple model providers, local Hugging Face models, structured outputs, chains, runnables, document loaders, and text splitters.

This repository is organized as a set of small, self-contained examples. Each script focuses on one concept so you can study, run, and modify the code independently.

## What This Project Covers

- Direct LLM calls with Groq.
- Chat-style interactions with system and human messages.
- Local and hosted Hugging Face model workflows.
- Embeddings for semantic search and similarity workflows.
- Structured outputs using Pydantic, TypedDict, and JSON-shaped responses.
- LangChain chains, including simple, sequential, parallel, and conditional patterns.
- Runnable primitives for composing workflows.
- Document loading from text, PDFs, directories, and web pages.
- Text splitting for chunking long documents into smaller pieces.

## Project Structure

The repository uses numbered lesson folders. The most important examples are:

| Path | Purpose |
| --- | --- |
| `main.py` | Minimal entry point that prints a hello message. |
| `1)LLMS/llm.py` | Basic `ChatGroq` invocation with a single prompt. |
| `2)Chat_Models/chat_model.py` | Chat model example using `SystemMessage` and `HumanMessage`. |
| `2)Chat_Models/huggingface_chat_model.py` | Hugging Face chat example using `ChatHuggingFace`. |
| `3)LocalModels/hugging_face.py` | Local Hugging Face pipeline example with `distilgpt2`. |
| `4)Embedding_models/huggingFace_embeddings.py` | Embedding generation with `HuggingFaceEmbeddings`. |
| `5)Structured_outputs/structured_outputs/json_schema.py` | Example JSON structure for output formatting. |
| `5)Structured_outputs/structured_outputs/ps.py` | Pydantic model example. |
| `5)Structured_outputs/structured_outputs/typed_Dict.py` | TypedDict example for structured data. |
| `5)Structured_outputs/structured_outputs/pydantic_ex.py` | Structured output extraction with `with_structured_output`. |
| `5)Structured_outputs/unstructured_outputs/output_parsers1.py` | Output parser example using `StringOutputParser`. |
| `6)Chains/simple_chain/simple_chain.py` | Prompt -> model -> parser chain. |
| `6)Chains/sequential_chain/sequential_chain.py` | Sequential chain that generates a report and then summarizes it. |
| `6)Chains/parallel_chain/parallel_chain.py` | Parallel chain that generates notes and a quiz before merging results. |
| `6)Chains/condtional_chain/conditional_chain.py` | Conditional routing example for math vs general queries. |
| `7)Runnables/part1/runnable1.py` | Basic runnable-style workflow example. |
| `7)Runnables/part2/Runnable_Sequence.py` | Runnable sequence example. |
| `7)Runnables/part2/Runnable_Parallel.py` | Runnable parallel example. |
| `8)Document_Loaders/TextLoader/code.py` | Load plain text documents from a `.txt` file. |
| `8)Document_Loaders/PyPdfLoader/code.py` | Load PDF documents page by page. |
| `8)Document_Loaders/DirectoryLoader/code.py` | Load many files from a directory. |
| `8)Document_Loaders/WebBasedLoader/code.py` | Load content from a web page. |
| `9TextSplitters/CharacterTextSplitting.py` | Character-based text chunking example. |
| `9TextSplitters/TextStructuredSpliting.py` | Notes on recursive text splitting. |

## Requirements

- Python 3.12+
- A virtual environment is recommended
- Internet access for hosted model and loader examples
- API keys in a `.env` file for any provider-specific scripts you run

## Installation

### Using `uv`

```bash
uv pip install -r requirements.txt
```

### Using `pip`

```bash
pip install -r requirements.txt
```

## Environment Variables

Some scripts call hosted model providers or use external services. Create a `.env` file in the repository root and add the keys you need for the examples you want to run.

Common variables include:

```env
GROQ_API_KEY=your_groq_key
OPENAI_API_KEY=your_openai_key
GOOGLE_API_KEY=your_google_key
ANTHROPIC_API_KEY=your_anthropic_key
HUGGINGFACEHUB_API_TOKEN=your_hugging_face_token
```

You do not need every key for every script. Add only the ones required by the file you are running.

## How To Run

Run each example directly from the repository root. Because the folders are numbered, quote the path when needed.

```bash
python "1)LLMS/llm.py"
python "2)Chat_Models/chat_model.py"
python "3)LocalModels/hugging_face.py"
python "4)Embedding_models/huggingFace_embeddings.py"
python "6)Chains/simple_chain/simple_chain.py"
python "8)Document_Loaders/TextLoader/code.py"
python "9TextSplitters/CharacterTextSplitting.py"
```

If you are using Windows PowerShell, the same commands work as long as you run them from the project root and activate your virtual environment first.

## Notes

- The numbered folders are meant to keep the examples organized by topic.
- Most scripts are intentionally small and educational rather than production ready.
- Some examples depend on current LangChain package structure, so newer packages such as `langchain-community`, `langchain-huggingface`, and `langchain-text-splitters` are included.
- The document loader and splitter examples are useful starting points for RAG pipelines.

## Repository Goal

This project is best used as a reference while learning LangChain. It shows how to move from simple prompt calls to richer workflows such as structured outputs, chain composition, runnable orchestration, and document preprocessing.
