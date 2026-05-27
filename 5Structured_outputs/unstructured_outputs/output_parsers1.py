# Output Parsers in Langchain

# String Output Parser
from langchain.output_parsers import StringOutputParser

# Example usage of StringOutputParser
string_parser = StringOutputParser()
output = string_parser.parse("This is a simple string output.")
print(output)  # Output: This is a simple string output. 