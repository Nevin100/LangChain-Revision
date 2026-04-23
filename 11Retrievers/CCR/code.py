from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_groq import ChatGroq
from langchain_community.retrievers import ContextualCompressionRetriever
from langchain_community.document_compressors import (
    LLMChainExtractor,
    LLMChainFilter,
    EmbeddingsFilter,
    DocumentCompressorPipeline
)
from langchain_text_splitters import CharacterTextSplitter
import os

# ============================================================
# CONTEXTUAL COMPRESSION RETRIEVAL - All 4 Compressor Types
# ============================================================
# Definition:
#   Normal retrieval returns FULL documents even if only 1-2 lines are relevant.
#   Contextual Compression retrieves docs first, then compresses/filters each doc
#   down to only the parts relevant to your query — using LLM or embeddings.
#
# Flow:
#   Query → Base Retriever → Full Docs → Compressor → Compressed Relevant Snippets
# ============================================================

# ------------------------------------------------------------
# SETUP — Documents, Embeddings, VectorStore, LLM
# ------------------------------------------------------------

docs = [
    Document(page_content="Langchain is a framework for building LLM applications. It was created by Harrison Chase in 2022.", metadata={"source": "doc1"}),
    Document(page_content="Langchain enables chaining of components for LLM workflows. It supports Python and JavaScript.", metadata={"source": "doc2"}),
    Document(page_content="MMR stands for Maximal Marginal Relevance. MMR improves diversity in document retrieval by penalizing redundant results.", metadata={"source": "doc3"}),
    Document(page_content="Vector stores like Chroma and FAISS store embeddings for fast similarity search.", metadata={"source": "doc4"}),
]

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_store = Chroma.from_documents(docs, embeddings)
base_retriever = vector_store.as_retriever(search_kwargs={"k": 4})

llm = ChatGroq(model="llama3-70b-versatile", temperature=0)

query = "Who created Langchain and what does it support?"

# ------------------------------------------------------------
# HELPER
# ------------------------------------------------------------

def print_results(title, results):
    print(f"\n{'='*60}")
    print(f" {title}")
    print(f"{'='*60}")
    if not results:
        print("  No results returned.")
    for i, doc in enumerate(results):
        print(f"  {i+1}. [{doc.metadata.get('source')}] {doc.page_content}")


# ============================================================
# TYPE 1 — LLMChainExtractor
# ============================================================
# Definition:
#   Passes each retrieved doc + query to the LLM and asks it to extract
#   ONLY the relevant sentences/phrases. If nothing is relevant in a doc,
#   that doc is dropped entirely.
#
# Use when:
#   - You need precise snippet extraction
#   - Docs are long and noisy
#   - Accuracy > speed/cost
# ============================================================

extractor_compressor = LLMChainExtractor.from_llm(llm)

extractor_retriever = ContextualCompressionRetriever(
    base_compressor=extractor_compressor,
    base_retriever=base_retriever
)

extractor_results = extractor_retriever.invoke(query)
print_results("TYPE 1 — LLMChainExtractor (extracts relevant snippets via LLM)", extractor_results)


# ============================================================
# TYPE 2 — LLMChainFilter
# ============================================================
# Definition:
#   LLM does a YES/NO decision per doc — is this doc relevant to the query?
#   Relevant docs are returned AS-IS (full content). Irrelevant docs are dropped.
#   No extraction happens — it's purely a filter.
#
# Use when:
#   - You want full doc content but without irrelevant docs
#   - Docs are already short/clean
#   - You want cheaper LLM usage than Extractor
# ============================================================

filter_compressor = LLMChainFilter.from_llm(llm)

filter_retriever = ContextualCompressionRetriever(
    base_compressor=filter_compressor,
    base_retriever=base_retriever
)

filter_results = filter_retriever.invoke(query)
print_results("TYPE 2 — LLMChainFilter (keeps/drops full docs via LLM yes/no)", filter_results)


# ============================================================
# TYPE 3 — EmbeddingsFilter
# ============================================================
# Definition:
#   No LLM involved. Computes cosine similarity between each doc's embedding
#   and the query embedding. Docs above the similarity_threshold are kept,
#   rest are dropped. Fast and cheap.
#
# Use when:
#   - Production / cost-sensitive environments
#   - Low latency required
#   - Approximate filtering is acceptable
# ============================================================

embeddings_filter_compressor = EmbeddingsFilter(
    embeddings=embeddings,
    similarity_threshold=0.5   # tune between 0.4 - 0.8 based on your data
)

embeddings_filter_retriever = ContextualCompressionRetriever(
    base_compressor=embeddings_filter_compressor,
    base_retriever=base_retriever
)

embeddings_results = embeddings_filter_retriever.invoke(query)
print_results("TYPE 3 — EmbeddingsFilter (filters by cosine similarity, no LLM)", embeddings_results)


# ============================================================
# TYPE 4 — DocumentCompressorPipeline
# ============================================================
# Definition:
#   Chains multiple compressors/transformers sequentially.
#   Each step's output becomes the next step's input.
#   Common pattern: Split docs into chunks → Filter chunks by embedding similarity
#   This gives chunk-level precision without any LLM call.
#
# Use when:
#   - Docs are very long (need chunking first)
#   - You want best quality without per-doc LLM calls
#   - Combining cheap filtering with smart splitting
# ============================================================

splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0,
    separator=". "
)

chunk_embeddings_filter = EmbeddingsFilter(
    embeddings=embeddings,
    similarity_threshold=0.5
)

pipeline_compressor = DocumentCompressorPipeline(
    transformers=[splitter, chunk_embeddings_filter]  # step1: split, step2: filter chunks
)

pipeline_retriever = ContextualCompressionRetriever(
    base_compressor=pipeline_compressor,
    base_retriever=base_retriever
)

pipeline_results = pipeline_retriever.invoke(query)
print_results("TYPE 4 — DocumentCompressorPipeline (split → embeddings filter)", pipeline_results)


# ============================================================
# SUMMARY
# ============================================================
# | Compressor              | LLM? | Speed  | Cost   | Best For                        |
# |-------------------------|------|--------|--------|---------------------------------|
# | LLMChainExtractor       | Yes  | Slow   | High   | Precise snippet extraction      |
# | LLMChainFilter          | Yes  | Slow   | Medium | Noise doc removal, full content |
# | EmbeddingsFilter        | No   | Fast   | Low    | Production, cost-sensitive      |
# | DocumentCompressorPipeline | No | Medium | Low   | Long docs, chunk-level filtering|
# ============================================================