"""
file: printedWords.py
assignment: task 2
language: python 3
author: Ethan Chang
Open the files and it will calculate total number of printed words for each year.
"""

import wordData
import matplotlib.pyplot as plt

def printedWords(words):
    """
    Converts words dictionary into a list covering up tuples of years, and total count words for each year.

    :param words: a dictionary of words and has another dictionary inside which includes years and counts
    :return: a list that contains tuples of years and total count words for each year, it will be sorted in ascending order
    """

    year_tuple = ()

    for year in words.values():

        year_list = tuple(year.items())
        year_tuple += year_list

    sort_tuple = sorted(year_tuple)

    return list(sort_tuple)

def wordsForYear(year, yearList):
    """
    Takes the inputted year by the user and searches the total number of counts for that year in yearList.

    :param year: an inputted year by the user
    :param yearList: list of tuples that has been sorted in ascending order of year
    :return: total number of printed words for the year user inputted, if empty then it returns 0
    """

    total = 0

    if year is None or year == " ":
        return 0

    else:

        for i in range(len(yearList)):

            numYear = yearList[i][0]
            count = yearList[i][1]

            if str(year) == str(numYear):

                total += count

        return total

def graph_plot(yearList):
    """
    Takes list of years and appends values to the lists that can be either list_of_years or list_of_counts, these 2 lists represent for the graph.

    :param yearList: list of tuples that has been sorted in ascending order of year
    :return: list_of_years and list_of_counts, both will be used for the graph
    """

    list_of_years = []
    list_of_counts = []

    for year in yearList:
        list_of_years.append(year[0])

    for j in range(len(yearList)):

        total_count = 0

        for k in range(len(yearList)):

            countCount = yearList[k][1]

            if yearList[k][0] == list_of_years[j]:

                total_count += countCount

        list_of_counts.append(total_count)

    return list_of_years, list_of_counts

def main():
    """
    Reads the files and the inputs by the user, will be placed into functions to find total printed words in specific year.

    :return: total printed words in a specific year and a graph
    """

    data_input = input("Enter word file: ")

    words = wordData.readWordFile(data_input)

    year = input("Enter year: ")

    yearList = printedWords(words)

    total = wordsForYear(year, yearList)

    print("Total printed words in " + str(year) + ": " + str(total))

    list_of_years, list_of_counts = graph_plot(yearList)

    plt.plot(list_of_years, list_of_counts)
    plt.show()

if __name__ == "__main__":
    main()