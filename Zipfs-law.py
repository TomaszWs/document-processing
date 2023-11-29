# Project Objec+ve:
# Analyse and try to comprehend Zipf’s Law.
# Write a Python script to analyze and visualize Zipf's Law for a set of words
# in different text
# corpora corresponding to different years.
# Steps:
import math

# File Input:
# Write code to read data from mulAple text files, each represenAng a different
# year's
# corpus. The data is tab-separated, with columns indicaAng the rank, word, and
# frequency.

# Zipf's Law Calcula5on:
# Implement a funcAon (zipf) to calculate metrics related to Zipf's Law for a
# given
# word. This should include calculaAons for frequency, rank, and other relevant
# staAsAcs.

# Word Selec5on:
# Allow the user to input a list of words they are interested in analyzing.
# Ensure the
# code can handle a variable number of words.

# Data Analysis:
# Iterate through the data and apply the zipf funcAon to each word of interest.
# Collect
# the results for further analysis.

# Visualiza5on:
# Use matplotlib or another ploOng library to visualize the Zipfian distribuAon
# for the
# selected words. Consider different types of visualizaAons such as scaPer
# plots, line
# charts, or bar charts.

# Corpus Comparison:
# Extend the script to compare the Zipfian distribuAons across different
# corpora
# (years). Consider how the word frequency distribuAon changes over Ame.
# Sta5s5cal Analysis:
# Enhance the script to calculate addiAonal staAsAcs or metrics related to word
# frequency and Zipf's Law. Explore other linguisAc features or characterisAcs
# that can
# be derived from the given data.


import matplotlib.pyplot as plt
import math


def files_reading():
    lines = []
    with open(r"2007.txt", "r", encoding="utf8") as text:
        for line in text:
            line = line.rstrip()
            if line:
                rank, current_word, frequency = line.split("\t")
                lines.append([rank, current_word, frequency])
    total_words = len(lines)
    print(total_words)
    return lines, total_words


def zipf(words, lines, total_words):
    ranks = []
    frequencies = []
    log_ranks = []
    log_frequencies = []
    for word in words:
        found = False
        for line in lines:
            if line[1] == word:
                found = True

                rank = int(line[0])
                occurrences = int(line[2])
                frequency = total_words / occurrences

                log_frequency = math.log(frequency)
                log_rank = math.log(rank)
                ranks.append(rank)
                frequencies.append(frequency)

                log_ranks.append(log_rank)
                log_frequencies.append(log_frequency)

                print(f"The rank of '{word}' is: {rank}")
                print(f"The number of occurrences of '{word}': {occurrences}")
                print(f"The frequency of '{word}' is: {frequency}")
                print(f"The log frequency of '{word}' is: {log_frequency}")
                print(f"The log rank of '{word}' is: {log_rank}\n")
                break
        if not found:
            print(f"'{word}' not found in the list.")
    return ranks, frequencies, log_ranks, log_frequencies


def plot_zipf(log_ranks, log_frequencies):
    plt.scatter(log_ranks, log_frequencies, marker='o', color='b')
    plt.xlabel('Log Rank')
    plt.ylabel('Log Frequency')
    plt.title('Zipf\'s Law')
    plt.show()


lines, total_words = files_reading()
words_to_check = ["el", "la", "como", "y", "dinero"]
ranks, frequencies, log_ranks, log_frequencies = zipf(words_to_check, lines, total_words)
plot_zipf(log_ranks, log_frequencies)
