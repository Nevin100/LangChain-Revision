from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the Hugging Face pipeline
llm = HuggingFacePipeline.from_model_id(
    repo_id="distilgpt2", # Replace with the appropriate model repository
    task="text-generation", # Replace with the appropriate task
    pipeline_kwargs= 
    # Optional: Additional arguments for the pipeline, such as temperature, max_new_tokens, etc.
        dict(
            temperature=0.7,
            max_new_tokens=100,
    )
)

# Create the ChatHuggingFace model using the initialized pipeline
model = ChatHuggingFace(llm=llm)

# Invoke the model with a sample question and print the response
response = model.invoke("What is the capital of France?")

# Display the content of the response
print(response.content)



