# Exercise 1:
# 1. Read the JSON data from 'data1.json'.
# 2. Extract and print all the sentences.

import json

# file = open("C:/Users/Stani/Desktop/Document_processing/DP2/data.json")
# data = json.load(file)
# for i in data:
#     print(i["text"])
# file.close()

# Exercise 2:
# Sample NLP results
nlp_results = [
    {"text": "This is a sample sentence.", "tokens": ["This", "is", "a", "sample", "sentence", "."]},
    {"text": "Another sentence.", "tokens": ["Another", "sentence", "."]},
]
# 1. Create a JSON file to store the NLP results.
# 2. Write the NLP results to the JSON file in a structured format.

# nlp_file = open("nlp_results.json", "w")
# json.dump(nlp_results, nlp_file, indent=4)

# Exercise 3:
# 1. Read the JSON data from 'books.json'.
# 2. Find all books by a Author A.
# 3. Find books published after 2019.
# 4. Calculate the average publication year of the books.

# file = open("C:/Users/Stani/Desktop/Document_processing/DP2/library.json", "r")
# book_file = json.load(file)
# for i in book_file:
#     if "Author A" in i["author"]:
#         print(i)
# for i in book_file:
#     if i["year"] > 2019:
#         print(i)
# books_count = 0
# suma = 0
# for i in book_file:
#     suma += i["year"]
#     books_count+=1
# print(int(suma/books_count))
# file.close()

# Exercise 4:
# 1. Read the data from 'books.json' and 'authors.json'.
# 2. Combine the data to create a new JSON file that includes author names with book information.

books = open("C:/Users/Stani/Desktop/Document_processing/DP2/books.json", "r")
authors = open("C:/Users/Stani/Desktop/Document_processing/DP2/authors.json", "r")
book_file = json.load(books)
authors_file = json.load(authors)

combined = {}
for i in book_file:
    for x in authors_file:
        if i.get("id") == x.get("author_id"):
            combined.update({i.get("name"): x})
print(book_file)
new_library = open("new_library.json", "w")
json.dump(combined, new_library, indent=4)

books.close()
authors.close()