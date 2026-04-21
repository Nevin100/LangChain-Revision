# 4. WebBasedLoader 
# WebBasedLoader is a document loader that fetches and processes web pages. It can be used to extract text content from websites, which can then be used for various applications such as natural language processing, information retrieval, and more. It typically uses libraries like BeautifulSoup or requests to fetch and parse web content. It works very well for simple web pages, but may struggle with complex websites that rely heavily on JavaScript or dynamic content.
# Importantly one url -> one document, so if you want to load multiple urls, you need to create multiple instances of WebBasedLoader or use a loop to iterate through the urls and load them one by one.

from langchain_community.document_loaders import WebBaseLoader

# The url variable contains the web page URL that we want to load. In this case, it is a product page for an Acer Predator 21 X laptop on Flipkart.
url = "https://www.flipkart.com/acer-predator-21-x-intel-core-i7-7th-gen-7820hk-64-gb-1-tb-hdd-1-ssd-windows-10-home-16-gb-graphics-gx21-71-laptop/p/itm5b74c9f1b541e"

loader = WebBaseLoader(url)

# The load method fetches the web page content and processes it to extract the relevant information. It returns a list of documents, where each document contains the page content and metadata.
data = loader.load()

# The load method returns a list of documents, where each document is a dictionary containing the page content and metadata. In this case, since we are loading a single URL, we will have one document in the list. We can access the page content using the 'page_content' key of the document.
print(data[0].page_content)