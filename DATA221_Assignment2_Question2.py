# The first part is the same as Question 1
import string
# Learn about nltk on Geeksforgeeks
import nltk
from nltk.util import  bigrams

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

# Construct Bigrams
bigram_list = list(bigrams(clean_tokens))

# Count the frequency
word_pairs_count = {}
for pairs in bigram_list:
    if pairs in word_pairs_count:
        word_pairs_count[pairs] += 1
    else:
        word_pairs_count[pairs] = 1

# Sort the pairs by descending order
sorted_pairs = sorted(word_pairs_count.items(), key=lambda item: item[1], reverse=True)
top_pairs = 5
for pairs, count in sorted_pairs[:top_pairs]:
    print(f'{pairs[0]} {pairs[1]} -> {count}')


