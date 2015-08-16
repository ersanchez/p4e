#!/usr/bin/python

# open romeo.txt
# read it line by line
# split each line into a list of words
# read the list, check to see if the word is not already inside
# if the word is not already inside, append it to the list

# print the list in alpha-order

#fileName = raw_input("Enter the file name: ")
fileName = 'romeo.txt'

openedFile = open(fileName)

# make an empty list called listing to be used for storing words
wordList = list()

# read the list line by line and strip of the ending spaces and line return
for line in openedFile:
    readline = line.strip()
    readwords = readline.split()
    wordList.extend(readwords)

wordList.sort()
print wordList

