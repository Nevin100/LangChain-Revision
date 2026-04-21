# RunnableParallel in Langchain : RunnableParallel is a primitive in Langchain that allows you to execute multiple Runnables in parallel. This can be useful when you have independent tasks that can be executed simultaneously, improving efficiency and reducing overall execution time and the results from all the Runnables will be collected and returned as a dictionary.

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnableSequence
from langchain_core.output_parsers import StrOutputParser

# Load environment variables from .env file
load_dotenv()

# Prompt initialization
prompt1 = PromptTemplate(
    template='Write a joke about {topic}',  
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Explain the concept of {topic} in simple terms',  
    input_variables=['topic']
)

# Model Initialization
model = ChatGroq(model="llama-3.1-8b-instant", temperature=0.4) 

# Parser initialization
parser = StrOutputParser()

# RunnableSequence for the first task (joke generation)
joke_chain = RunnableSequence(  
    prompt1,
    model,
    parser
)

# RunnableSequence for the second task (concept explanation)
explanation_chain = RunnableSequence(  
    prompt2,
    model,
    parser
)

# Create a RunnableParallel that combines both RunnableSequences. This will allow us to execute both tasks simultaneously.
parallel_chain = RunnableParallel(
    joke_chain=joke_chain,
    explanation_chain=explanation_chain
)

# Now we can invoke the parallel chain with a specific topic. The `invoke` method will execute both RunnableSequences in parallel and return a dictionary containing the results from both chains.
result = parallel_chain.invoke({'topic': 'Narendra Modi'})

# The result will be a dictionary containing the outputs from both RunnableSequences. We can access the joke and the explanation using the keys 'joke_chain' and 'explanation_chain' respectively.
print("Joke:", result['joke_chain'])
print("Explanation:", result['explanation_chain'])