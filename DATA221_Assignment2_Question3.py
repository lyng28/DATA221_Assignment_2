import string

with open('sample-file.txt', 'r') as file:
    file_lines = file.readlines()

# Remove punctuation everywhere in the text, code learnt from this Geeksforgeeks website
# https://www.geeksforgeeks.org/python/python-remove-punctuation-from-string/
remove_punctuation = str.maketrans("","", string.punctuation)

# Create a dictionary consists of cleaned line and the line number and original line
