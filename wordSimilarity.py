"""
file: wordSimilarity.py
assignment: task 4
language: python 3
author: Ethan Chang
Open the files and returns list of top 5 words that are similar to each other.
"""

import wordData
import math

def topSimilar(words, word):
    """
    Gives out a list of top 5 words in descending order.

    :param words: a dictionary of words and has another dictionary inside which includes years and counts
    :param targetword: a string or word, inputted by the user and it's used to find similar words
    :return: list of top 5 words including input word and makes it into descending order of similarity, if list got nothing then it only returns a word
    """

    matrix = {}

    empty_list = []

    if word in words:

        for term in words:

            matrix[term] = list(words[term].values())

            total = 0
            for item in matrix[term]:
                total += (item * item)

            norm = (math.sqrt(total))

            for i in range(len(matrix[term])):
                matrix[term][i] /= norm

        sim = list()
        vw = matrix[word]

        for compound in words:
            vc = matrix[compound]
            w_sim = 0

            for i in range(len(vw)):
                w_sim += vw[i] * vc[i]

            sim.append((compound, w_sim))

        sorted_sim = sorted(sim, key = lambda x: x[1], reverse = True)

        tuple_list = sorted_sim[:5]

        similarity_list = []

        for char in tuple_list:
            similarity_list.append(char[0])

        return similarity_list

    else:
        empty_list.append(word)
        return empty_list

def main():
    """
    Reads the files, picks up the input of year the user inputted and tries to find word that are similar. Then prints out top 5 similar words.

    :return: a list of top 5 similar words in descending order
    """

    data_input = input("Enter word file: ")

    words = wordData.readWordFile(data_input)

    word = input("Enter word: ")

    top_similar = topSimilar(words, word)

    print("The most similar words are: ")

    print(top_similar)

if __name__ == "__main__":
    main()