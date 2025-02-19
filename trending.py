"""
file: trending.py
assignment: task 3
language: python 3
author: Ethan Chang
Open the files and returns top and bottom trending words from starting and ending year.
"""

import wordData

def trending(words, startYr, endYr):
    """
    Builds a list of tuples for each word, it will be sorted in decreasing trend value. Specific words and values will be picked from startYr to endYr.

    :param words: a dictionary of words and has another dictionary inside which includes years and counts
    :param startYr: an integer that represents starting year of trending words
    :param endYr: an integer that represents ending year of trending words
    :return: a list of tuples for each word, will be sorted in decreasing value
    """

    word_list = list(words.keys())
    trend_list = []

    for word in word_list:
        if word in words:
            start_key = words[word].keys()

            if startYr in start_key:
                value_startYr = words[word][startYr]

                end_key = words[word].keys()

                if endYr in end_key:
                    value_endYr = words[word][endYr]

                    if value_startYr >= 1000 and value_endYr >= 1000:

                        trend = value_endYr / value_startYr

                        trend_list.append((word, trend))

    sorted_trend = sorted(trend_list, key = lambda x: x[1], reverse = True)

    return sorted_trend

def topbottom_trend(sorted_trend):
    """
    Iterates over the sorted_trend list of tuples and adds the values to either top trend or bottom trend list.

    :param sorted_trend: a list of tuples containing years and trend values
    :return: top and bottom list, top represents top trending words and bottom represents bottom trending words
    """

    top = []
    bottom = []

    i = 0
    while i < 10:

        if i < len(sorted_trend):

            top_sort = sorted_trend[i][0]

            if top_sort is None:
                break

            top.append(top_sort)
            i += 1
        else:

            break

    j = 1
    while j < 11:

        if j < len(sorted_trend):

            bottom_sort = sorted_trend[-j][0]

            if bottom_sort is None:
                break

            bottom.append(bottom_sort)
            j += 1

        else:
            break

    return top, bottom

def main():
    """
    Reads the files, gets the user inputs of startYr and endYr. When passed to the trending() function, main function receives a list of trending words and outputs top and bottom lists.

    :return: list of words that represent top trending words and bottom trending words that are from startYear to end year
    """

    data_input = input("Enter word file: ")
    words = wordData.readWordFile(data_input)

    start_input = int(input("Enter starting year: "))

    end_input = int(input("Enter ending year: "))

    sorted_trend = trending(words, start_input, end_input)

    top, bottom = topbottom_trend(sorted_trend)

    print("The top 10 trending words from " + str(start_input) + " to " + str(end_input) + ": ")

    for word in top:
        print(word)

    print("")

    print("The bottom 10 trending words from " + str(start_input) + " to " + str(end_input) + ": ")

    for word in bottom:
        print(word)

if __name__ == "__main__":
    main()