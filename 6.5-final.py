#!/usr/bin/python

# 

text = 'X-DSPAM-Confidence:    0.8475'

colonSpace = text.find(':')

afterColon = text[colonSpace+1:]

targetValue = float(afterColon)

print targetValue 
