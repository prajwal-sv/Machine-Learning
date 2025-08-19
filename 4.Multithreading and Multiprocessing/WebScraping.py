#Web Scraping

# Web scraping is the process of extracting data from websites. It can be done using various libraries in Python, such as BeautifulSoup, Scrapy, and requests.

#https://www.langchain.com/resources
#https://www.langchain.com/testing-guide-ebook
#https://www.langchain.com/careers


import threading
import requests
from bs4 import BeautifulSoup

url = [

    'https://www.langchain.com/resources' ,
    'https://www.langchain.com/testing-guide-ebook',
    'https://www.langchain.com/careers'

]

def fetch_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(f"charater in Url in {url}: {len(soup.text)}")

threads = []
# Create a thread for each URL and start it

for u in url:
    thread = threading.Thread(target=fetch_url, args=(u,))
    threads.append(thread)
    thread.start()

for thread in threads :
    thread.join()
print("All URLs have been processed.")