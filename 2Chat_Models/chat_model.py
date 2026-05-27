from langchain_groq import ChatGroq
# langchain.core messages provides the HumanMessage and SystemMessage classes for structuring messages in a conversation
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Initialize the ChatGroq LLM with specified model and temperature
chat = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.4
)

# Invoke the LLM with a sample prompt using a list of messages
messages = [
    SystemMessage(content="You are a helpful assistant.You are smart and everything."),
    HumanMessage(content="Who is better Rahul gandhi or Narendra Modi?")
]

# Invoke the chat model with the list of messages and print the response
response = chat.invoke(messages)

# Print the content of the response
print(response.content)
