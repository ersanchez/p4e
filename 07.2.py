#!/usr/bin/python

# prompt for a file name
# open file
# read file
# look for lines
# count lines
# extract floating point values
# computer average of floating point values

filename = raw_input("Enter file name: ")
fileopen = open(filename)
count = 0
total = 0
for line in fileopen:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    count = count + 1
    value = float(line[20:])
    total = total + value
# print count
# print total
print 'Average spam confidence:',total/count
