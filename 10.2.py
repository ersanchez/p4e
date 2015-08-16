#!/usr/bin/python

# read mbox-short.txt
# determine the hour that each msg was sent
# count the number of emails per hour
# print a listing of hours, and number of emails for each hour
###################################################
# get the filename, if it is not at least one character,
# assing the filename mbox-short.txt

filename = raw_input("Enter filename: ")
if len(filename) < 1:
  filename = "mbox-short.txt"
openedfile = open(filename)

countedhours = dict()

# ignore all lines that don't start with 'From '

for line in openedfile:
    fromline = line.split()
    if len(fromline) == 0:
        continue
    if fromline[0] != 'From':
        continue
    sendtime = fromline[5]
    delimiter = ':'
    sendinfo = sendtime.split(delimiter)
    senthour = sendinfo[0]
    if senthour not in countedhours:
        countedhours[senthour] = 1
    else:
        countedhours[senthour] += 1

countedlist = list()

for key, val in countedhours.items():
    countedlist.append( (key, val) )

countedlist.sort()

for key, val in countedlist:
    print key, val

