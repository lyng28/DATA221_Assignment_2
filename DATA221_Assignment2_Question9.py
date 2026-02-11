from bs4 import BeautifulSoup
import requests
import csv

from urllib3.filepost import writer

# Request to parse the information from the html
machine_learning_wiki_html = requests.get('https://en.wikipedia.org/wiki/Machine_learning', headers={'User-Agent': 'Mozilla/5.0'}).text
parsed_html_document = BeautifulSoup(machine_learning_wiki_html, 'html.parser')

# Find the main content div
main_article_content = parsed_html_document.find('div', id='mw-content-text')

# Extract the first table that has more than 3 data rows
first_table = None
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
headers = []
header_cells = first_table.find_all('th')
if header_cells:
    for th in header_cells:
        headers.append(th.get_text())
else:
    first_row = table_rows[0]
    column_count = len(first_row.find_all(['td', 'th']))
    for number in range(column_count):
        headers.append(f'col{number + 1}')

# Extract data rows
table_data = []
for row in table_rows:
    cells = row.find_all('td')
    if not cells:
        continue
    row_data = []
    for cell in cells:
        row_data.append(cell.get_text())
    table_data.append(row_data)

with open('wiki-table.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(table_data)

