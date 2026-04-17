from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableLambda
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Prompt 1: Generate detailed notes about a given document
prompt1 = PromptTemplate(
    template='Generate detailed notes about: {document}',
    input_variables=['document']
)

# Prompt 2: Generate a quiz based on the given document
prompt2 = PromptTemplate(
    template='Generate a quiz based on: {document}',
    input_variables=['document']
)

# Prompt 3: Merge the original document, generated notes, and quiz into a cohesive summary or report
prompt3 = PromptTemplate(
    template='Merge notes and quiz.\nDocument: {document}\nNotes: {notes}\nQuiz: {quiz}',
    input_variables=['document', 'notes', 'quiz']
)

# LLMs
llm1 = ChatGroq(model="llama-3.1-8b-instant", temperature=0.4)
llm2 = ChatGroq(model="llama-3.1-8b-instant", temperature=0.4)
llm3 = ChatGroq(model="llama-3.1-8b-instant", temperature=0.4)

# Output parser
parser = StrOutputParser()

# Chains
chain1 = prompt1 | llm1 | parser
chain2 = prompt2 | llm2 | parser

# Parallel Execution of notes and quiz generation using RunnableParallel. RunnableParallel is a LangChain utility that allows multiple chains to run simultaneously, improving efficiency and reducing overall execution time.
parallel_chain = RunnableParallel(
    notes=chain1,
    quiz=chain2
)

# Merge step to combine the outputs of the parallel chains with the original document
def merge_fn(inputs):
    merged_prompt = prompt3.format(
        document=inputs['document'],
        notes=inputs['notes'],
        quiz=inputs['quiz']
    )
    return merged_prompt

# Create a chain for merging the outputs of the parallel chains with the original document and generating a final summary or report using llm3 using RunnableLambda to define a custom function for merging the inputs and then passing it through llm3 and the parser to get the final output. This step ensures that the final output is cohesive and integrates all the generated content effectively.
merge_chain = RunnableLambda(merge_fn) | llm3 | parser

# Final chain that takes the original document, runs the parallel chains to generate notes and quiz, and then merges everything together to produce a final output
final_chain = (
    {
        "document": lambda x: x["document"],  
        "notes": parallel_chain.pick("notes"),
        "quiz": parallel_chain.pick("quiz")
    }
    | merge_chain
)

# Run the final chain with a specific document and print the result
result = final_chain.invoke({
    "document": "LangChain is a framework for building LLM applications. It provides tools and abstractions to help developers create applications that can interact with language models in a more structured and efficient way. With LangChain, you can easily create chains of prompts and LLM calls, manage state across interactions, and build complex applications that leverage the power of language models. Whether you're building a chatbot, a question-answering system, or any other application that requires natural language understanding and generation, LangChain provides the tools you need to get started quickly and efficiently."
})

# Print the final result, which includes the original document, generated notes, and quiz merged into a cohesive summary or report
print(result)