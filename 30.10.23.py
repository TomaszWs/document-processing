# import nltk
# from nltk.book import *

# text = text1
# licznik = 0
# words = []
# for word in text:
#     if len(word) == 4:
#         words.append(word.lower())
#         licznik += 1
# print(words)
# print("ile slow: ",licznik)

# text = text1
# licznik = 0
# words = []
# for word in text:
#     if len(word) > 17:
#         words.append(word.lower())
#         licznik +=1
# print(words)
# print("ile slow: ",licznik)

# import nltk
# from nltk.book import *
# sentences = [sent1, sent2, sent3, sent4, sent5, sent6, sent7, sent8, sent9]
# list_of_dictionaries = []
# for sentence in sentences:
#     sent_set = set(sentence)
#     sent_dict = []
#     for word in sorted(sent_set):
#         if word.isalpha():
#             sent_dict.append(word.lower())
#     list_of_dictionaries.append(sorted(sent_dict))
#
# joint_dictionary = []
# for sent_dict in list_of_dictionaries:
#     for word in sent_dict:
#         if word not in joint_dictionary:
#             joint_dictionary.append(word)
#
# print(sorted(joint_dictionary))


import nltk
from nltk.book import *

# Define vocab_size() function, which for a given text will return the size of a
# dictionary (so return a number of all unique words). How many are there in each
# book?


# def vocab_size(text):
#     dict_size = len(set(text))
#     return dict_size
#
#
# text = text1
# dict_size = vocab_size(text1)
# print(dict_size)


# Print the 10 most commonly occurring words in text1.
# text = [word.lower() for word in text1 if word.isalpha()]
# fdist = nltk.FreqDist(text)
# words = fdist.most_common(10)
# print(words)


# Check which words are the longest in each of the text.

import nltk
from nltk.book import *

texts = [text1, text2, text3, text4, text5, text6, text7, text8, text9]
longest = []

for text in texts:
    longest_word = ""
    length = 0
    for word in text:
        word = word.lower()
        if len(word) > length and word.isalpha():
            longest_word = word
            length = len(word)
    longest.append(longest_word)

print(longest)
