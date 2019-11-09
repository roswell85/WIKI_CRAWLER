# WIKI_CRAWLER
A Wikipedia crawler that takes in a wikipedia link and extracts paragraph texts from the link\n and the hyperlinks within the mentioned link
Author : Ali Shawky
download wikicrawler.py and its requirements.txt 
import wikicrawler
create a crawler object using the constructor 
>>> crawler = wikicrawler.WIKI_CRAWLER()
the user will be asked to input a valid wikipedia link 
the crawler object has 2 empty lists : crawler.links and crawler.paragraphs and 2 main bounded methods; crawler.get_links() & crawler.get_paragraphs() that are called to append hyperlink and text data to the input page respectively
the user will be asked to choose an integer less than the length of crawler.links so that it knows which pages to query and search for more text in.

Uses: wikicrawler extracts text data for further use in NLP neural models such as RNN or LSTM
