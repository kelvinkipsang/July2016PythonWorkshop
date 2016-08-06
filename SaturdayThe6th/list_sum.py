#!/usr/bin/env python
"""
Create a function that gets the sum of all the digits in a list given as a parameter

"""


def sum_digits(a):
	'''
		Takes a list A
			-Returns the sum of all the digits in a list
	'''
	# Code goes here:
	list=[]
	for x in a:
		x=str(x)
		for ch in x:
			list.append(int(ch))



	sum=0
	for y in list:
		sum+=y

	print sum




sum_digits([11,30,45])
"""
Test cases include:

sum_digits([10,30,45])
	----This should return 13

"""