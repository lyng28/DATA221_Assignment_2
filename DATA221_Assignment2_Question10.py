def find_lines_containing(filename, keyword):
    match_lines = []
    line = 1
    with open(filename, 'r') as file:
        for text in file:
            if keyword.lower() in text.lower(): # Check for case-insensitive
                match_lines.append((line, text.strip('\n')))
            line += 1
    return match_lines

# Test case using sample-file.txt and lorem as the text
test_case = find_lines_containing('sample-file.txt', 'lorem')

print(f'Total matching lines are: ', len(test_case))
print(f'The first 3 matching lines are: ')
for line_number, line_text in test_case[:3]:
    print(f'{line_number}: {line_text}')


