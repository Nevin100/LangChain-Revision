# 2. PyPdfLoader
# It is a loader that uses the PyPDF2 library to extract text from PDF files. It can handle both local files and URLs. It uses PyPdf Library to read PDF files and extract text from them. Importantly not great for scanned PDFs as it does not perform OCR.Works well for text-based PDFs.Each page is treated as a separate document, allowing for more granular processing. It is a good choice for extracting text from PDFs that are primarily text-based and do not require OCR.
# one page -> one document

from langchain_community.document_loaders import PyPDFLoader

# Create an instance of the PyPDFLoader class, providing the path to the PDF file you want to load.
loader = PyPDFLoader("pdf-sample.pdf")

# The load method reads the PDF file and returns a list of documents, where each document corresponds to a page in the PDF. Each document contains the text content of the page, as well as metadata such as the page number.
pages = loader.load()

# Each page is treated as a separate document, allowing for more granular processing.
print(pages[0].page_content)