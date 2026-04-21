# Text Spliiting in LangChain
# It is often necessary to split large documents into smaller chunks for processing. LangChain provides various text splitters to help with this task. Text Splitting is a crucial step in many natural language processing tasks, such as document summarization, question answering, and information retrieval. By breaking down large texts into manageable pieces, we can improve the efficiency and accuracy of our models.

# Advantages: 
# 1. Improved Performance: Smaller chunks of text can be processed more efficiently by language models, leading to faster response times and reduced computational resources. 
# 2. Better Context Management: Splitting text allows for better context management, enabling models to focus on relevant information without being overwhelmed by large volumes of data. 
# 3. Enhanced Accuracy: By breaking down complex documents into smaller sections, we can improve the accuracy of tasks such as summarization and question answering, as the model can better understand and analyze the content. 
# 4. Improves Semantic Understanding: Text splitting can help models better understand the structure and meaning of the text, leading to more accurate interpretations and responses.
# 5. Facilitates Parallel Processing: By splitting text into smaller chunks, we can enable parallel processing, allowing multiple sections of text to be processed simultaneously, further improving efficiency.
# 6. Reduces Hallucination: By providing smaller, more focused chunks of text, we can reduce the likelihood of models generating irrelevant or incorrect information, leading to more accurate and reliable outputs. 

# Types of Text Spliting Technique :
# 1. Length Based :
# in this text splitting technique, the text is divided into chunks based on a specified length. This can be useful for ensuring that each chunk is of a manageable size for processing by language models. For example, you can split a document into chunks of 500 characters or 100 words.
# -> each chunk contains metadata and content. The metadata includes information about the chunk, such as its position in the original text, while the content is the actual text of the chunk.

from langchain_text_splitters import CharacterTextSplitter

# A sample text is defined, which will be used as input for the text splitting process. This text describes a scene in space, with vivid imagery and descriptions of celestial phenomena.
text = """
    Drifting beyond the edge of mapped constellations, a silent vessel glides through the velvet dark where starlight feels ancient and unfinished. Nebulae bloom like cosmic ink spills, painting the void with hues no human language has named. Somewhere, a distant pulsar ticks like a forgotten clock, measuring time in bursts of light instead of seconds.

    Fragments of asteroid dust shimmer like frozen whispers, tracing the echoes of collisions that happened before memory itself. Planets spin in quiet obedience to invisible forces, their surfaces holding storms, silence, and stories yet to be imagined. In the vast stretch between galaxies, there is no up or down—only the slow, eternal unfolding of everything that ever was and ever will be.

    And in that immeasurable stillness, space does not feel empty. It feels patient.
"""

# A `CharacterTextSplitter` object is created with specific parameters: `chunk_size`, `chunk_overlap`, and `separator`. The `chunk_size` parameter defines the maximum number of characters in each chunk, while the `chunk_overlap` parameter allows for a specified number of characters to overlap between consecutive chunks. The `separator` parameter defines how the text should be split, in this case, by double newlines.
splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=20, separator="\n\n")

# The `split_text` method is called on the `splitter` object, passing the input text as an argument. This method will return a list of text chunks based on the specified parameters.
result = splitter.split_text(text)

# The `chunk_size` parameter specifies the maximum number of characters in each chunk, while the `chunk_overlap` parameter allows for a specified number of characters to overlap between consecutive chunks. The `separator` parameter defines how the text should be split, in this case, by double newlines.
print(result)

