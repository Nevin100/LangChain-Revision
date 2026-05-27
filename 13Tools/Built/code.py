# Tools : 
# Tools in langchain are used to perform specific tasks, such as searching the web, retrieving data from a database, or performing calculations. They can be used in conjunction with agents to help them accomplish their goals.

# There are wide variety of tools available in langchain, including:
# - Search tools: These tools allow agents to search the web for information. Examples include DuckDuckGoSearchRun, GoogleSearchRun, and BingSearchRun.
# - Data retrieval tools: These tools allow agents to retrieve data from databases or APIs. Examples include SQLDatabaseTool, APIEndpointTool, and JSONTool.
# - Calculation tools: These tools allow agents to perform calculations. Examples include CalculatorTool and PythonREPLTool. etc.

# Example : 
# In this example, we will use the DuckDuckGoSearchRun tool to search for the capital of France.
from langchain_community.tools import DuckDuckGoSearchRun

# Create an instance of the DuckDuckGoSearchRun tool
searchtool = DuckDuckGoSearchRun()

# Use the tool to search for the capital of France
results = searchtool.invoke("What is the capital of France?")

# Display the results
print(results)