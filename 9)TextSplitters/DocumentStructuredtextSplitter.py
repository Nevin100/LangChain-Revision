# 3. Document Structured Text Splitter
# The `DocumentStructuredTextSplitter` is a text splitting technique that focuses on maintaining the structure of the original document while splitting it into smaller chunks. This method is particularly useful for documents that have a clear structure, such as articles, reports, or any text with headings and subheadings. The `DocumentStructuredTextSplitter` ensures that the chunks created retain the logical flow and organization of the original document, making it easier for language models to understand and process the content effectively.

# Language attribute in RecursiveCharacterTextSplitter is used to specify the language of the text being split. This can help the splitter to better understand the structure and grammar of the text, which can lead to more accurate splitting. For example, if the language is set to English, the splitter may recognize sentence boundaries and paragraph breaks more effectively, resulting in chunks that are more coherent and easier for language models to process.

from langchain_text_splitters import RecursiveCharacterTextSplitter, Language 

text = """"
    document = "Sample Title", "This is the content of the sample document. It contains multiple sentences and paragraphs to demonstrate the DocumentStructuredTextSplitter."
"""

# Create an instance of the DocumentStructuredTextSplitter with the specified language, chunk size, and chunk overlap
splitter = RecursiveCharacterTextSplitter(language=Language.ENGLISH, chunk_size=150, chunk_overlap=10)

# Split the text into chunks
chunks = splitter.split_text(text)

# Print the split chunks
print(chunks)


