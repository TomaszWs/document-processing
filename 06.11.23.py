# Task 1
# For each of the texts from the NLTK Book, please select two words and write
# code that returns common contexts in which these words occur.

# import nltk
# from nltk.book import *
#
# word1 = "Elinor"
# word2 = "Marianne"
#
#
# def commoncontexts(word1,word2):
#     for text in [text1, text2, text3, text4, text5, text6, text7, text8, text9]:
#         book_text = nltk.Text(text)
#         print(f"\nIn {text.name}")
#         common_contexts = book_text.common_contexts([word1, word2])
#
#
# commoncontexts(word1,word2)


# Task 2
# Check the differences in WordNet resources (https://wordnet.princeton.edu/)
# and the WordNet corpus in NLTK. Find examples of the same synsets and
# examples of WordNet synsets that do not appear in the NLTK corpus.

# import nltk
# from nltk.corpus import wordnet
#
# print(wordnet.synsets('dog'))


# Task 3
# For the word 'sweet' find hyponyms.

# import nltk
# from nltk.corpus import wordnet
#
# hyponyms = []
# synsets_sweet = wordnet.synset("sweet.a.02")
# print(synsets_sweet.hyponyms())

# for synset in synsets_sweet:
#     hyponyms.extend(synset.hyponyms())
#
# for hyponym in hyponyms:
#     print(hyponym.name())

# synset_sweet = wordnet.synsets("sweet")[2]
# hyponyms = synset_sweet.hyponyms()
# for hyponym in hyponyms:
#     print(hyponym.name())

# Task 4
# Use the WordNet corpus to calculate the distance between concepts:
# (a) 'wood' and 'metal'
# (b) 'run' and 'walk'

# import nltk
# from nltk.corpus import wordnet
#
# synset1 = wordnet.synset('wood.n.01')
# synset2 = wordnet.synset('metal.n.01')
# synset3 = wordnet.synset('run.v.01')
# synset4 = wordnet.synset('walk.v.01')
#
# similarity1 = synset1.wup_similarity(synset2)
# print(f"Similarity for wood and metal': {similarity1}\n")
# similarity2 = synset3.wup_similarity(synset4)
# print(f"Similarity for run and walk': {similarity2}")


# Task 5
# Find the 10 most frequently occurring words in the corpus  inaugural

# import nltk
# from nltk.corpus import brown, inaugural
#
# words = inaugural.words()
# fdist = nltk.FreqDist(words)
# most_frequent = fdist.most_common(10)
# print(most_frequent)

# Task 6
# write a script to check how often the words 'mountains' 'ocean' and 'Bungee jump'
# appear in the brown corpus in the adventure category

import nltk
from nltk.corpus import brown, inaugural

words = ["mountains", "ocean", "Bungee jump"]
word_freq = {word: 0 for word in words}

for word in words:
    matching_words = [w for w in brown.words(categories='adventure') if w.lower() == word.lower()]
    word_freq[word] = len(matching_words)

for word, frequency in word_freq.items():
    print(f"{word} : {frequency}")
