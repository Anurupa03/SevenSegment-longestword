import re

fileOpen = open("words.txt", "r")  # opens the file in read mode
words = fileOpen.read().splitlines()  # puts the file into an array
fileOpen.close()

longest_letter_length = 0
longest_word = ''
longest_accepted_word_list = list()
pattern = '[gkmqwxz]' #gkmqwxz

for test_words in words:
    if len(test_words) < longest_letter_length:
        continue
    bad_letters = re.findall(pattern, test_words)
    if bad_letters:
        continue
    if len(test_words) == longest_letter_length:
        longest_accepted_word_list.append(test_words)
        longest_word = test_words
    if len(test_words) > longest_letter_length:
        longest_letter_length = len(test_words)
        longest_accepted_word_list.clear()
        longest_accepted_word_list.append(test_words)
        longest_word = test_words

print(longest_letter_length, longest_word,longest_accepted_word_list)
