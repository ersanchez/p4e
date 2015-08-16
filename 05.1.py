#!/usr/bin/python

# Read a list of numbers until "done" is entered.
# Then print out the following:
# * total
# * count
# * average
# If the user enters anything other than a number, print an error message
# and go to the next number

count = 0
total = 0

while True:
    inputvalue = raw_input('Enter a number: ')
    if inputvalue == 'done':
        break
    if len(inputvalue) < 1:
        break   # checks for empty line
    num = float(inputvalue)
    count = count + 1
    total = total + num
print 'Invalid data'
print count
print total
average = total / count
print average
