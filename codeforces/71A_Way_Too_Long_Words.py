from sys import stdin 

f = stdin

num_of_words = int(f.readline())

for word in f:
    stripped_word = word.strip()
    word_length = len(stripped_word)
    if word_length > 10:
        res = stripped_word[0] + str(len(stripped_word[1: word_length - 1])) + stripped_word[-1]
        print(res.strip())
    else:
        print(stripped_word)