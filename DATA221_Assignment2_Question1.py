import string

with open('sample-file.txt', 'r') as file:
    file_content = file.read()

# Split into token based on whitespace
original_tokens = file_content.split()

# Clean each token
clean_tokens = []
for letter in original_tokens:
    letter = letter.lower() # Lowercase all tokens
    letter = letter.strip(string.punctuation) # Remove punctuation in front and after each letter

    # Count the Alphabetic Letters for each token
    letter_count = 0
    for alphabetic_letters in letter:
        if alphabetic_letters.isalpha():
            letter_count += 1

    # Add the token into token list if the Alphabetic Letters is at least 2
    if letter_count >= 2:
        clean_tokens.append(letter)

# Count the frequencies of words
word_count = {}
for word in clean_tokens:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Sort the word in descending order
sorted_word = sorted(word_count.items(), key=lambda item:(-item[1], item[0]))
top_word = 10
for word, count in sorted_word[:top_word]:
    print(f'{word} -> {count}')

file.close()
