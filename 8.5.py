#!/usr/bin/python

# open 'mbox-short.txt'
# search for lines that start with 'From'
# extract the email address from the 'From' lines
# print 'There are XX lines in the file with From as the first word'

count = 0                   # resets the counter
fromEmail = None            # resets fromEmail

filename = raw_input('Enter file name: ')
# filename = 'mbox-short.txt'

openedFile = open(filename)

for line in openedFile:
    readline = line.strip()
    if not line.startswith('From '):    # ignores lines not starting From
        continue
    lineWords = readline.split()    # splits line into a list
    fromEmail = lineWords[1]        # sets fromEmail = 2nd item in list
    print fromEmail                 # prints fromEmail
    count = count + 1

print'There were', count, 'lines in the file with From as the first word'
