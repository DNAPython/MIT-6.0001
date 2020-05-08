# -*- coding: utf-8 -*-
"""
Created on Fri May  8 00:02:43 2020

@author: DNAPython@gmail.com et. al. Got help from 

https://github.com/angelichorsey/mit-eecs/blob/master/course_6_0001/problem-sets/ps1/ps1b.py

got stuck on doing monthly contribution outside the while loop. my ps1a.py solution was far less elegant. 
I enjoy more () for my own sanity. 
"""

# get user inputs

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input('Enter the semi-annual raise, as a decimal: '))

# set givens
portion_down_payment = 0.25
r = 0.04
current_savings = 0.0
months = 0

# raises and ROI caclulations looping over again until down payment is reached.
while current_savings < (total_cost*portion_down_payment):
    monthly_salary = (annual_salary/12)
    current_savings += ((monthly_salary*portion_saved)+(current_savings*r/12))
    months += 1
   
    if months % 6 == 0:
        annual_salary += (annual_salary*semi_annual_raise)

# final output
print('Number of months:', months)
