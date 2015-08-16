#!/usr/bin/python

# 

text = 'X-DSPAM-Confidence:    0.8475'

colonSpace = text.find(':')
print colonSpace

print colonSpace+1

afterColon = text[colonSpace+1:]

print afterColon

targetValue = float(afterColon)

print targetValue 
