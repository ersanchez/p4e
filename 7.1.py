#!/usr/bin/python

# prompt for a file name
# open the file
# read the file
# print the contents in upper case

filename = raw_input("Enter file name: ")
fileopen = open(filename)
for line in fileopen:
    line = line.rstrip()
    print line.upper()
