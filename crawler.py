import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 2
    while page <= max_pages :
        url = 'http://books.toscrape.com/catalogue/page-' + str(page) + '.html'
        source_code = requests.get(url)
        #print(source_code)
        plain_text = source_code.text
        #print(plain_text)
        soup = BeautifulSoup(plain_text,'html.parser')
        print(soup.find_all('a', {'title'}))
        for link in soup.find_all('a'):
            href = link.get('href')
            print('http://books.toscrape.com/'+href)
        page+=1



trade_spider(6)
