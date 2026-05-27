from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Initialize the Hugging Face endpoint with the appropriate repository and task
llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="chat-completion",     
)

# Create the ChatHuggingFace model using the initialized endpoint
model = ChatHuggingFace(llm=llm)

# Invoke the model with a sample question and print the response
response = model.invoke("What is the capital of France?")

# Display the content of the response
print(response.content)
