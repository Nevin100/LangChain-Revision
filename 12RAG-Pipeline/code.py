# Creating a Rag piepeline to fetch the transcript of a YouTube video and answer questions based on it.

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_groq import ChatGroq
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.runnables import RunnablePassthrough

# Load the environment variables from the .env file 
load_dotenv()

# (A) Document Indexing
# step - 1 - (Document Indexing) - Fetch the transcript of a YouTube video

video_id = "mEsleV16qdo" # Youtube video ID
try:
    # Fetch the transcript for the given video ID 
    ytt = YouTubeTranscriptApi()
    transcript_list = ytt.fetch(video_id, languages=['en'])
    
    # Combine the transcript entries into a single string
    transcript = " ".join(entry.text + " " + str(entry.start) + " " + str(entry.duration) for entry in transcript_list)

    # Print the transcript
    print("Transcript fetched successfully and Document Indexing (1a) is done.")
    print (transcript)

except TranscriptsDisabled:
    # If transcripts are disabled for the video, print a message and set transcript to an empty string
    print("Transcripts are disabled for this video.")
    transcript = ""

    
# step - 2 - (Document Indexing) - Split the transcript into smaller chunks using RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1400, 
    chunk_overlap=350
)
chunks = text_splitter.split_text(transcript)
print(f"Transcript split into {len(chunks)} chunks.")
print("Chunks created successfully and Document Indexing (1b) is done.")

# step - 3 - (Document Indexing) - Create a vector store using FAISS and HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_store = FAISS.from_texts(
    texts=chunks, 
    embedding=embeddings,
)
print("Vector store created successfully and Document Indexing (1c & 1d) is done.")
print(f"Number of documents in vector store: {vector_store.index.ntotal}")
print(vector_store.index_to_docstore_id)

# (B) Retrieval
# step - 4 - (Retrieval) - Create a retriever from the vector store
retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 3})

# (C) Augmentation
# step - 5 - Create a ChatGroq agent and use the retriever to fetch relevant chunks of the transcript based on a user query
llm = ChatGroq(
    model="llama-3.3-70b-versatile", 
    temperature=0.7, 
    max_tokens=2048
)

# step - 6 - Create a prompt template for the agent to answer questions based on the retrieved chunks 
prompt = PromptTemplate(
    input_variables=["question", "retrieved_chunks"],
    template="""
    You are a helpful assistant that answers questions based on the retrieved chunks of a YouTube video transcript.
    
    Question: {question}
    
    Retrieved Chunks:
    {retrieved_chunks}
    If you don't know the answer, say you don't know.
    Please provide a concise and accurate answer to the question based on the retrieved chunks. 
    """
)

# (D) Generation 
# step - 7 - Create a function to answer questions using the ChatGroq agent and the retriever
# def answer_question(question):
#     # Retrieve relevant chunks based on the question
#     retrieved_chunks = retriever.invoke(question)
    
#     # Format the retrieved chunks for the prompt
#     retrieved_chunks_text = "\n".join([chunk.page_content for chunk in retrieved_chunks])
    
#     # Create the prompt with the question and retrieved chunks
#     formatted_prompt = prompt.format(question=question, retrieved_chunks=retrieved_chunks_text)
    
#     # Get the answer from the ChatGroq agent
#     answer = llm.invoke(formatted_prompt)
    
#     return answer

# OR

# step - 7 - Create a chain to answer questions using the ChatGroq agent and the retriever
# LCEL Chain: RunnableParallel -> Sequential
chain = (
    {
        # Parallel - 1: Retrieve relevant chunks and format them
        "retrieved_chunks": retriever | (lambda docs: "\n".join(d.page_content for d in docs)),
        # Parallel - 2: Pass the question as-is
        "question": RunnablePassthrough()
    }
    # Sequential - 1: Format the prompt
    | prompt
    # Sequential - 2: Get the answer from the LLM
    | llm
    # Sequential - 3: Parse the output to string
    | StrOutputParser()
)

# usage :
user_question = "What is the main topic of the video?"
answer = chain.invoke(user_question)

# Print the question and the answer
print(f"Question: {user_question}")
print(f"Answer: {answer}")
 
