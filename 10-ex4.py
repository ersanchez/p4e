#!/usr/bin/python

# count words in a file
# determine the most commonly-used words
# print the 

filename = open('romeo.txt')
countedwords = dict()

for line in filename:
    wordlist = line.split()
    for word in wordlist:
        countedwords[word] = countedwords.get(word, 0) + 1

finallist = list()
for key, val in countedwords.items():
    finallist.append( (val, key) )

finallist.sort(reverse=True)

for val, key in finallist[:10]:
    print key, val
