from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Initialize the ChatGroq LLM with specified model and temperature
# temperature controls the randomness of the output. if 0, the output will be deterministic and for 1 is the most random.
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)

# Invoke the LLM with a sample prompt
response = llm.invoke("What is the capital of India?")
print(response.content)
