#!/usr/bin/env python
"""
Create a function that:
	1. Halves even numbers
	2. Doubles odd numbers
	3. Returns the sum of all
"""

def super_sum(num):
	# Your awesome code flows from here
    for x in num:
        if x%2==0:
            even=x/2
            print "halved even number:" + str(even)

        elif x%2!=0:

            odd = x * 2
            print "doubled odd number :" + str(odd)
        else:
            print
    print odd +even


super_sum([20,9])








