from bs4 import BeautifulSoup
import requests

# Request to parse the information from the html
data_science_wiki_html = requests.get('https://en.wikipedia.org/wiki/Data_science', headers={'User-Agent': 'Mozilla/5.0'}).text
parsed_html_document = BeautifulSoup(data_science_wiki_html, 'html.parser')

# Extract the <h2> section heading
main_article_content = parsed_html_document.find('div', id='mw-content-text')
h2_section_headings = main_article_content.find_all('h2')

excluded_headings = ['References', 'External links', 'See also', 'Notes']

headings = []
for heading in h2_section_headings:
    heading_text = heading.get_text()
    heading_text = heading_text.replace('[edit]', ' ').strip()

    # Skip the headings include the word in excluded_headings:
    if any(word in heading_text for word in excluded_headings):
        continue

    if heading_text != '':
        headings.append(heading_text)

# Save the headings into txt file
with open('headings.txt', 'w') as file:
    for heading in headings:
        file.write(heading + '\n')


