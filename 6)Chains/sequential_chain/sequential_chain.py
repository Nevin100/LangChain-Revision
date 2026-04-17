# Q.) topic -> llm -> report -> llm -> summary + recommendations
# Implement a sequential chain that takes a topic as input, generates a report about it using an LLM, and then summarizes and provides recommendations for the report using another LLM. (as explained from flow diagram above this question)

from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables from a .env file
load_dotenv()

# Define a prompt template for generating a detailed report about a given topic. The prompt instructs the model to act as a helpful assistant and produce a comprehensive report based on the input topic.
prompt = PromptTemplate(
    template='You are a helpful assistant. Generate a detailed report about {topic}',
    input_variables=['topic']
)
 
# Define a prompt template for summarizing the report, which takes the generated report as input and instructs the model to summarize it concisely while extracting key points.
summary_prompt = PromptTemplate(
    template='Summarize the following report in a concise manner and make sure to extract the key points: {report}',
    input_variables=['report']
)

# Initialize the ChatGroq model with the specified model and temperature
model = ChatGroq(
    model="llama-3.1-8b-instant", 
    temperature=0.4
)

# Create an output parser that will parse the output of the model into a string format
parser = StrOutputParser()

# Create separate chains for report generation and summary generation
report_chain = prompt | model | parser 
summary_chain = summary_prompt | model | parser

# Chain the report generation and summary chains together. The output of the report chain will be passed as input to the summary chain.
sequential_chain = report_chain | summary_chain

# Invoke the sequential chain with a specific topic (in this case, 'typhoid fever') and store the result in the variable 'summary_result'
summary_result = sequential_chain.invoke({'topic': 'typhoid fever'})

# Print the structure of the sequential chain
print(summary_result)