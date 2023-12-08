import nltk
from nltk.book import *
#
# print(text1.concordance("monstrous"))
# print(text1.similar("monstrous"))
# print(text2.common_contexts(["monstrous", "very"]))
# print(text4.dispersion_plot(["citizens", "democracy", "freedom", "duties",
#                              "America"]))
# print(text3.generate())
# print(len(text3))
# print(sorted(set(text3)))
# print(len(set(text3)))
#
# # Lexical richness of the text
# print(len(text3) / len(set(text3)))
#
# print(text3.count("smote"))
# print(100 * text5.count("lol") / len(text5))
#
#
# def lexical_diversity(text):
#     return len(text) / len(set(text))
#
#
# def percentage(count, total):
#     return 100 * count / total
#
# print("Lexical diversity of text3: ", lexical_diversity(text3))
# print("Lexical diversity of text5: ", lexical_diversity(text5))
# print("percentage: ", percentage(4, 5))
# print("Percentage of \"a\" in text4: ", percentage(text4.count('a'), len(text4)))


# 1.8 Exercises
# 1. ○ Try using the Python interpreter as a calculator, and typing expressions like 12 /
# (4 + 1).

print(12 / (5+1))

# 2. ○ Given an alphabet of 26 letters, there are 26 to the power 10, or 26 ** 10, 10-
# letter strings we can form. That works out to141167095653376L (the L at the end
# just indicates that this is Python’s long-number format). How many hundred-letter
# strings are possible?

print(26 ** 100)

# 3. ○ The Python multiplication operation can be applied to lists. What happens when
# you type ['Monty', 'Python'] * 20, or 3 * sent1?

print(['Monty', 'Python'] * 20)

# 4. ○ Review Section 1.1 on computing with language. How many words are there in
# text2? How many distinct words are there?

print(len(text2))
print(len(set(text2)))

# 5. ○ Compare the lexical diversity scores for humor and romance fiction in Ta-
# ble 1-1. Which genre is more lexically diverse?

# Romance

# 6. ○ Produce a dispersion plot of the four main protagonists in Sense and Sensibility:
# Elinor, Marianne, Edward, and Willoughby. What can you observe about the
# different roles played by the males and females in this novel? Can you identify the
# couples?

protagonists = ["Elinor", "Marianne", "Edward", "Willoughby"]
# text2.dispersion_plot(protagonists)

# 7. ○ Find the collocations in text5.

text5.collocations()

# 8. ○ Consider the following Python expression: len(set(text4)). State the purpose
# of this expression. Describe the two steps involved in performing this computation.

# Expression creates the set of unique words in text4, and then returns the
# number of unique words

# 9. ○ Review Section 1.2 on lists and strings.
# a. Define a string and assign it to a variable, e.g., my_string = 'My String' (but
# put something more interesting in the string). Print the contents of this variable
# in two ways, first by simply typing the variable name and pressing Enter, then
# by using the print statement.

string = "Lorum ipsem"
print(string)

# b. Try adding the string to itself using my_string + my_string, or multiplying it
# by a number, e.g., my_string * 3. Notice that the strings are joined together
# without any spaces. How could you fix this?

string += " Ipsem lorum"
print(string)

# 10. ○ Define a variable my_sent to be a list of words, using the syntax my_sent = ["My",
# "sent"] (but with your own words, or a favorite saying).
# a. Use ' '.join(my_sent) to convert this into a string.

my_sent = ["My","sent","is","not","my","sent"]
sent = " ".join(my_sent)
print(sent)

# b. Use split() to split the string back into the list form you had to start with

print(sent.split())

# 11. ○ Define several variables containing lists of words, e.g., phrase1, phrase2, and so
# on. Join them together in various combinations (using the plus operator) to form
# whole sentences. What is the relationship between len(phrase1 + phrase2) and
# len(phrase1) + len(phrase2)?

phrase1 = ["1","2223"]
phrase2 = ["3","44"]
phrase3 = ["5","635"]
phrase4 = ["7","86"]
phrase5 = ["9","08"]

print(phrase5+phrase2)
print(len(phrase1 + phrase2))
print(len(phrase1) + len(phrase2))

# 12. ○ Consider the following two expressions, which have the same value. Which one
# will typically be more relevant in NLP? Why?
# a. "Monty Python"[6:12]
# b. ["Monty", "Python"][1]

# Option a - operation on strings, more important in NLP

# 13. ○ We have seen how to represent a sentence as a list of words, where each word is
# a sequence of characters. What does sent1[2][2] do? Why? Experiment with other
# index values.

# sent1[2][2] extracts third character from third word in the nested list

# 14. ○ The first sentence of text3 is provided to you in the variable sent3. The index of
# the in sent3 is 1, because sent3[1] gives us 'the'. What are the indexes of the two
# other occurrences of this word in sent3?

print(sent3)
print([index for index, word in enumerate(sent3) if word == "the"])

# 15. ○ Review the discussion of conditionals in Section 1.4. Find all words in the Chat
# Corpus (text5) starting with the letter b. Show them in alphabetical order.



# 16. ○ Type the expression range(10) at the interpreter prompt. Now try range(10,
# 20), range(10, 20, 2), and range(20, 10, -2). We will see a variety of uses for this
# built-in function in later chapters.
# 17. ◑ Use text9.index() to find the index of the word sunset. You’ll need to insert this
# word as an argument between the parentheses. By a process of trial and error, find
# the slice for the complete sentence that contains this word.
# 18. ◑ Using list addition, and the set and sorted operations, compute the vocabulary
# of the sentences sent1 ... sent8.
# 19. ◑ What is the difference between the following two lines? Which one will give a
# larger value? Will this be the case for other texts?
# >>> sorted(set([w.lower() for w in text1]))
# >>> sorted([w.lower() for w in set(text1)])
# 20. ◑ What is the difference between the following two tests: w.isupper() and not
# w.islower()?
# 21. ◑ Write the slice expression that extracts the last two words of text2.
# 22. ◑ Find all the four-letter words in the Chat Corpus (text5). With the help of a
# frequency distribution (FreqDist), show these words in decreasing order of fre-
# quency.
# 23. ◑ Review the discussion of looping with conditions in Section 1.4. Use a combi-
# nation of for and if statements to loop over the words of the movie script for
# Monty Python and the Holy Grail (text6) and print all the uppercase words, one
# per line.
# 24. ◑ Write expressions for finding all words in text6 that meet the following condi-
# tions. The result should be in the form of a list of words: ['word1', 'word2', ...].
# a. Ending in ize
# b. Containing the letter z
# c. Containing the sequence of letters pt
# d. All lowercase letters except for an initial capital (i.e., titlecase)
# 25. ◑ Define sent to be the list of words ['she', 'sells', 'sea', 'shells', 'by',
# 'the', 'sea', 'shore']. Now write code to perform the following tasks:
# a. Print all words beginning with sh.
# b. Print all words longer than four characters
# 26. ◑ What does the following Python code do? sum([len(w) for w in text1]) Can
# you use it to work out the average word length of a text?
# 27. ◑ Define a function called vocab_size(text) that has a single parameter for the
# text, and which returns the vocabulary size of the text.
# 28. ◑ Define a function percent(word, text) that calculates how often a given word
# occurs in a text and expresses the result as a percentage.
# 29. ◑ We have been using sets to store vocabularies. Try the following Python expres-
# sion: set(sent3) < set(text1). Experiment with this using different arguments to
# set(). What does it do? Can you think of a practical application for this?