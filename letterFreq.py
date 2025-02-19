"""
file: letterFreq.py
assignment: task 1
language: python 3
author: Ethan Chang
Opens the files then returns English lower case alphabet letters in decreasing order
"""

import wordData
import matplotlib.pyplot as plt

def letterFreq(words):
    """
    Looks through the dictionary to find number of counts with each lowercase character and then sorts them in decreasing order.

    :param words: a dictionary of words and has another dictionary inside which includes years and counts
    :return: a string that has all 26 English lower case letters that's been sorted in decreasing order
    """

    letter_count = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}

    for word in words:
        occ = wordData.totalOccurrences(word, words)
        for char in word:

            letter_count[char] += occ

    x = list(letter_count.items())

    y = sorted(x, key = lambda x:x[1], reverse = True)

    sorted_dict = dict(y)

    key_list = list(sorted_dict.keys())

    line = ""

    for letter in key_list:
        line += letter

    return line

def bar_graph(words):
    """
    Gets the lists of letters and the list of # counts for each letters

    :param words: a dictionary of words and has another dictionary inside which includes years and counts
    :return: letter_counts list that has counts of each letters and letters list that has list of all English 26 letters but in lower case
    """

    letter_counts = []

    letter_count = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0,
                    "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0,
                    "y": 0, "z": 0}

    for word in words:

        occ = wordData.totalOccurrences(word, words)

        for char in word:

            letter_count[char] += occ

    letters = list(letter_count)

    for value in letter_count:

        val = letter_count[value]
        letter_counts.append(val)

    return letters, letter_counts

def main():
    """
    Reads the user input on data file, then starts execution on readWordFIle function.

    :return: a string of English lower case letters that's been sorted in decreasing order and a bar graph
    """

    data_input = input("Enter word file: ")

    words = wordData.readWordFile(data_input)

    line = letterFreq(words)
    k_list = list(line)

    string = ""

    for character in k_list:
        string += character[0]

    print("Letters sorted by decreasing frequency: " + string)

    letters, letter_counts = bar_graph(words)

    plt.bar(list(letters), list(letter_counts), color='skyblue')
    plt.show()


if __name__ == "__main__":
    main()