from bs4 import BeautifulSoup
import requests

# Request to parse the information from the html
data_science_wiki_html = requests.get('https://en.wikipedia.org/wiki/Data_science', headers={'User-Agent': 'Mozilla/5.0'}).text
parsed_html_document = BeautifulSoup(data_science_wiki_html, 'html.parser')

# Extract and print the page title
page_title = parsed_html_document.find("title")
if page_title is not None:
    print('Page title: ')
    print(page_title.get_text())
else:
    print('Page title not found.')

# Find the main content div
main_article_content = parsed_html_document.find('div', id='mw-content-text')
all_paragraph = main_article_content.find_all('p')

# Find the first paragraph that contains more than 50 words
first_paragraph_text = []
for paragraph in all_paragraph:
    paragraph_text = paragraph.get_text()
    if len(paragraph_text) >= 50:
        first_paragraph_text = paragraph_text
        break

print(first_paragraph_text)


