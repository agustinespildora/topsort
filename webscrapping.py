import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'Content-Type': 'application/json'
}

page = requests.get('https://quotes.toscrape.com', headers=headers)

soup = BeautifulSoup(page.text, 'html.parser')

quotes = []

quote_elements = soup.find_all('div', class_='quote')

for quote_element in quote_elements:
    # extracting the text of the quote
    text = quote_element.find('span', class_='text').text
    # extracting the author of the quote
    author = quote_element.find('small', class_='author').text

    # extracting the tag <a> HTML elements related to the quote
    tag_elements = quote_element.find('div', class_='tags').find_all('a', class_='tag')

    # storing the list of tag strings in a list
    tags = []
    for tag_element in tag_elements:
        tags.append(tag_element.text)
        
print(quote_elements[0])