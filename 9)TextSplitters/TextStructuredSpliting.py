# 2. Recursive Character Text Splitter:
# The Recursive Character Text Splitter is an extension of the basic character text splitter. It allows for more complex splitting strategies by recursively applying the splitting process to the resulting chunks. This can be particularly useful when dealing with hierarchical or nested structures in the text, such as paragraphs, sections, or chapters. The recursive approach enables finer control over the splitting process, allowing for more meaningful and contextually relevant chunks of text to be generated.

from langchain_text_splitters import RecursiveCharacterTextSplitter

# A sample text is defined, which will be used as input for the text splitting process. This text describes a scene in space, with vivid imagery and descriptions of celestial phenomena.
text = """
    Drifting beyond the edge of mapped constellations, a silent vessel glides through the velvet dark where starlight feels ancient and unfinished. Nebulae bloom like cosmic ink spills, painting the void with hues no human language has named. Somewhere, a distant pulsar ticks like a forgotten clock, measuring time in bursts of light instead of seconds.

    Fragments of asteroid dust shimmer like frozen whispers, tracing the echoes of collisions that happened before memory itself. Planets spin in quiet obedience to invisible forces, their surfaces holding storms, silence, and stories yet to be imagined. In the vast stretch between galaxies, there is no up or down—only the slow, eternal unfolding of everything that ever was and ever will be.

    And in that immeasurable stillness, space does not feel empty. It feels patient.
"""

# A `RecursiveCharacterTextSplitter` object is created with specific parameters: `chunk_size`, `chunk_overlap`, and `separator`. The `chunk_size` parameter defines the maximum number of characters in each chunk, while the `chunk_overlap` parameter allows for a specified number of characters to overlap between consecutive chunks. The `separator` parameter defines how the text should be split, in this case, by double newlines.
splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=20)

# The `split_text` method is called on the `splitter` object, passing the input text as an argument. This method will return a list of text chunks based on the specified parameters.
result = splitter.split_text(text)

# The `chunk_size` parameter specifies the maximum number of characters in each chunk, while the `chunk_overlap` parameter allows for a specified number of characters to overlap between consecutive chunks. The `separator` parameter defines how the text should be split, in this case, by double newlines.
print(result)
