import nltk
from nltk.book import *

print(text1.concordance("monstrous"))
print(text1.similar("monstrous"))
print(text2.common_contexts(["monstrous", "very"]))
print(text4.dispersion_plot(["citizens", "democracy", "freedom", "duties",
                             "America"]))
print(text3.generate())
print(len(text3))
print(sorted(set(text3)))
print(len(set(text3)))

# Lexical richness of the text
print(len(text3) / len(set(text3)))

print(text3.count("smote"))
print(100 * text5.count("lol") / len(text5))


def lexical_diversity(text):
    return len(text) / len(set(text))


def percentage(count, total):
    return 100 * count / total

print("Lexical diversity of text3: ", lexical_diversity(text3))
print("Lexical diversity of text5: ", lexical_diversity(text5))
print("percentage: ", percentage(4, 5))
print("Percentage of \"a\" in text4: ", percentage(text4.count('a'), len(text4)))
