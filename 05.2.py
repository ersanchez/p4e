#!/usr/bin/python

# repeated prompt a user for integer numbers until the user enters 'done'
# once 'done' is entered, print largest and smallest numbers
# if user types anything other than a valid number catch it with a try/except

largest = -1 
smallest = None
while :
    entered = raw_input('Enter a number: ')
    try: 
        number = float(entered)
        if number > largest:
            largest = number
        if smallest is None:
            smallest = number
        if test < smallest:
            smallest = number
    except:
        print "Invalid input"
        print "Maximum is",largest
        print "Minimum is",smallest

