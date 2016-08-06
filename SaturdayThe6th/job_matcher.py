#!/usr/bin/env python
"""
Given 50 randomly located drivers, map them to some random number of randomly located jobs such that
total distance to jobs is minimised. With 100 jobs available, map the driver ids and job location ids
and print out the result in a key value pair
"""
import random


drivers=[]
x=0
while x<51:
    drivers.append(random.randint(1,51))
    x+=1

jobs=[]
x=0
while x<51:
    jobs.append(random.randint(1, 51))
    x += 1


dicti=dict(zip(drivers,jobs))


print dicti