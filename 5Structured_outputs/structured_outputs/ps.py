# Question : How can I use the ChatGroq model to generate structured outputs in Python, specifically for summarizing a review and listing its pros and cons using structured outputs (typed dictionaries and Annotated)?

from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import TypedDict, List, Annotated

# Load environment variables from a .env file
load_dotenv()

# Initialize the ChatGroq LLM with specified model and temperature
model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.4
)

# Define a TypedDict to structure the output of the model
class ReviewSummary(TypedDict):
    summary: str
    pros: List[str]
    cons: List[str]
    sentiments: Annotated[str, "The overall sentiment of the review, e.g., positive, negative, neutral"]

# Use the with_structured_output method to specify that we want the output to be structured according to the ReviewSummary TypedDict
structured_result = model.with_structured_output(ReviewSummary)

# Invoke the structured_result with a prompt asking for a summary of a review, along with the pros and cons in list format
result = structured_result.invoke("Summarize the review and returns the pros and cons in list format. The Hardware is great but the software feels bloated. there are too many pre-installed apps that I don't use and they take up a lot of storage space. I wish there was an option to uninstall them or at least disable them.")

# Print the structured result
print(result)

print("Summary analyzed by LLM: ", result['summary'])  # Access the summary from the structured output
print("Pros analyzed by LLM: ", result['pros'])     # Access the list of pros from the structured output
print("Cons analyzed by LLM: ",result['cons'])     # Access the list of cons from the structured output
print("Sentiments analyzed by LLM:", result['sentiments'])  # Access the sentiments from the structured output
