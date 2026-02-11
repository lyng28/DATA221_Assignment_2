import string

with open('sample-file.txt', 'r') as file:
    file_lines = file.readlines()

# Remove punctuation everywhere in the text, code learnt from this Geeksforgeeks website
# https://www.geeksforgeeks.org/python/python-remove-punctuation-from-string/
remove_punctuation = str.maketrans("","", string.punctuation)

# Create a dictionary consists of cleaned line and the line number and original line
near_duplicate_lines = {}
line_number = 1

for line in file_lines:
    original_line = line.strip()
    if original_line == '': # Jump to next line if the line is blank after removing the whitespace
        line_number += 1 # Credited to ChatGPT help me debug this code
        continue

    lower_case_line = original_line.lower() # Convert line to all lowercase
    remove_punctuation_line = lower_case_line.translate(remove_punctuation)

    cleaned_line = ''.join(remove_punctuation_line.split()) # Learn about join() in the same website above

    if cleaned_line not in near_duplicate_lines:  # Add the cleaned line into the dictionary
        near_duplicate_lines[cleaned_line] = []
    near_duplicate_lines[cleaned_line].append((line_number,original_line))

    line_number += 1

# Indicate the sets that have more than one line
duplicates_sets = []
for sets in near_duplicate_lines.values():
    if len(sets) > 1:
        duplicates_sets.append(sets)

print('The total amount of near-duplicate sets: ', len(duplicates_sets))
print('The first two near-duplicate sets are: ')

for number in range(min(2, len(duplicates_sets))):
    print(f'Set {number + 1}: ')
    for line_number, text in duplicates_sets[number]:
        print(f'{line_number}: {text}')

