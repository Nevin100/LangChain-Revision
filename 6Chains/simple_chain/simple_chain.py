from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables from a .env file
load_dotenv()

# Define a prompt template that takes a topic as input and generates 5 interesting facts about it
prompt = PromptTemplate(
    template='Generate 5 interesting facts about {topic}',
    input_variables=['topic']
)

# Initialize the ChatGroq model with the specified model and temperature
model = ChatGroq(model='llama-3.1-8b-instant', temperature=0.3)

# Create an output parser that will parse the output of the model into a string format
parser = StrOutputParser()

# Chain the prompt, model, and parser together. The output of the prompt will be passed to the model, and the output of the model will be parsed by the parser.
chain = prompt | model | parser

# Invoke the chain with a specific topic (in this case, 'space exploration') and store the result in the variable 'result'
result = chain.invoke({'topic': 'space exploration '})

# Print the structure of the chain in an ASCII format for visualization
chain.get_graph().print_ascii()

# Print the result of the chain invocation, which should be a string containing 5 interesting facts about space exploration
print(result)

