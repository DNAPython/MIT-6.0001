# -*- coding: utf-8 -*-
# this is an example of the solution to MIT OCW problem set 0
# https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/assignments/I
# by DNAPython@gmail.com

import numpy as np
import math

# use open code to set decimal places to 2
def set_numpy_decimal_places(places, width=0):
    set_np = '{0:' + str(width) + '.' + str(places) + 'f}'
    np.set_printoptions(formatter={'float': lambda x: set_np.format(x)})

set_numpy_decimal_places(2)

#get x
x = int(input("select your x ? >")) 

#get y
y = int(input("select your y ? >"))

#raise x to the power of y
result = (x**y)

# return the result of the calculation
print(f"your x raised to the power of y is {result}")

# for some reason take the log of x in base 2
log_result = math.log(x,2)                      

# print the result
print(f"your result log is {log_result}")

