import nltk

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk import FreqDist

# text = ("Natural Language Processing (NLP) is a subfield of artificial "
#         "intelligence (AI) that focuses on the interaction between "
#         "computers and human language.")
# tokens = word_tokenize(text)
# stop_words = set(stopwords.words('english'))
# tokens_stop = [token for token in tokens if token not in stop_words]
# tags = pos_tag(tokens_stop)
# print(tags)

# text_2 = ("Barack Obama was born in Honolulu and served as the 44th President "
#         "of the United States. He is known for his charismatic speeches.")
#
# tokens = word_tokenize(text_2)
# tags = pos_tag(tokens)
# named = ne_chunk(tags)
# print(named)

# words = ['choice','chosen','choose']
# lemmatyzacja = WordNetLemmatizer()
# for word in words:
#     print(word, " : ", lemmatyzacja.lemmatize(word))
# ps = PorterStemmer()
# print('Stemming:')
# for word in words:
#     print(word, " : ", ps.stem(word))

text = ("In the heart of Silicon Valley, Apple Inc. is known for its "
        "innovative products and groundbreaking technologies. Founded by "
        "Steve Jobs, Steve Wozniak, and Ronald Wayne in Cupertino, "
        "California, Apple has become one of the world's most valuable "
        "companies, with a market capitalization of over $2 trillion. "
        "Tim Cook, the current CEO of Apple, has successfully led the company "
        "through various product launches, including the iPhone, iPad, "
        "MacBook, and Apple Watch. Meanwhile, in Seattle, Washington, "
        "Amazon.com Inc. reigns supreme in the e- commerce industry. "
        "Founded by Jeff Bezos, Amazon has grown to become the largest "
        "online retailer globally, offering a wide range of products and "
        "services. Amazon Web Services (AWS), a subsidiary of Amazon, "
        "provides cloud computing solutions to countless businesses worldwide.")

tokens = word_tokenize(text)
tagged = pos_tag(tokens)
NNP = [word for word,pos in tagged if pos == 'NNP']
NNP_string = ' / '.join(NNP)
# print(NNP_string)

# Remove stop words and tokenize the text below. Afterwards count the most
# frequent words.
tokens_inter = []
for token in tokens:
    if token.isalpha(): tokens_inter.append(token)

stop_words = set(stopwords.words('english'))
tokens_stop = [token for token in tokens_inter if token not in stop_words]
fdist = FreqDist(tokens_stop)
print(fdist.most_common())
