"""
file: wordData.py
assignment: task 0
language: python 3
author: Ethan Chang
Opens the files from the user input and returns dictionaries
"""

import wordData

def readWordFile(fileName):
    """
    Opens the text files and reads each line, and stores the text to word_data dictionary.

    :param: filename: name of the file
    :return: dictionaries of words as key and has another dictionary inside which includes years and counts
    """

    word_data = {}

    if 'data/' not in fileName:
        fileName = 'data/' + fileName

    with open(fileName) as file:

        for line in file:
            line = line.strip()
            tokens = line.split(',')

            if len(tokens) == 1:
                word = tokens[0]
                word_data[word] = dict()
                for i in range(1900, 2009):
                    word_data[word][i] = 0

            else:
                year = int(tokens[0])
                count = int(tokens[1])
                word_data[word][year] = count

    return word_data

def totalOccurrences(word, words):
    """
    Uses parameter, word that was inputted by user and checks to see if that specific word is inside the words dictionary then returns number count of that word.

    :param word: a word inputted by the user
    :param words: a dictionary of words and has another dictionary inside which includes years and counts
    :return: the number of counts of the word, if it's not in the dictionary then it returns 0
    """

    count = 0

    if word in words:

        in_words = words[word]

        for num in in_words.values():
            count += num

        return count

    else:
        return 0

def main():
    """
    Reads users inputs on data file, then reads another input on the word user is inputting.

    :return: total number of counts from a specific word the user inputted
    """

    data_input = input("Enter word file: ")
    word = input("Enter word: ")

    words = wordData.readWordFile(data_input)

    print("Total occurrences of " + word + ": " + str(wordData.totalOccurrences(word, words)))

if __name__ == "__main__":
    main()