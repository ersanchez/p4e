#!/usr/bin/python

# repeated prompt a user for integer numbers until the user enters 'done'
# once 'done' is entered, print largest and smallest numbers
# if user types anything other than a valid number catch it with a try/except

largest = -1 
smallest = None

while True :
    entered = raw_input('Enter an integer: ')
    try:
        entered = int(entered)
    except:
        print "Invalid input"
    if entered == 'done':
        break
    if entered > largest:
        largest = entered
    if smallest is None:
        smallest = entered
    if entered < smallest:
        smallest = entered
        
print "Maximum is",largest
print "Minimum is",smallest

