from bs4 import BeautifulSoup
import requests

# Request to parse the information from the html
machine_learning_wiki_html = requests.get('https://en.wikipedia.org/wiki/Machine_learning', headers={'User-Agent': 'Mozilla/5.0'}).text
parsed_html_document = BeautifulSoup(machine_learning_wiki_html, 'html.parser')

# Find the main content div
main_article_content = parsed_html_document.find('div', id='mw-content-text')

# Extract the first table that has more than 3 data rows
first_table =[]
for table in main_article_content:
    data_rows = table.find_all('tr')
    data_row_count = 0
    for data in data_rows:
        if data.find_all('td'):   # Find if the row contains data
            data_row_count += 1
    if data_row_count >= 3:
        first_table = table
        break

# Extract header rows from <th>
table_rows = first_table.find_all('tr')

