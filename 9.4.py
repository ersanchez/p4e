#!/usr/bin/python

# open 'mbox-short.txt'
# identify lines starting with 'From ' and take the second word (sender)
# create a dictionary that maps sender's email with count of messages 
# determine the name of the person who sent the most email

senderlist = dict()
filename = raw_input("Enter file name: ")
if len(filename) < 1:
    filename = "mbox-short.txt"
openedfile = open(filename)
for line in openedfile:
    fromline = line.split()
    if len(fromline) == 0:
        continue
    if fromline[0] != 'From:': 
        continue
    senderemail = fromline[1]
    if senderemail not in senderlist:
        senderlist[senderemail] = 1
    else:
        senderlist[senderemail] += 1
maxsender = None
maxcount = None
for key in senderlist:
    if senderlist[key] is None or senderlist[key] > maxcount:
        maxsender = senderemail
        maxcount = senderlist[key]
print maxsender, maxcount

