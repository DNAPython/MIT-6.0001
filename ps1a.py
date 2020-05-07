# -*- coding: utf-8 -*-
"""
Created on Wed May  6 23:06:43 2020

@author: DNAPython@gmail.com

"""


# Assume down payment of 25%
portion_down_payment = 0.25

# Assume you have 0 savings to start
current_savings = 0

# Assume investment rate of 4% 
r = 0.04 / 12

# Get annual salary
annual_salary = float(input("Enter your annual salary: "))

# Calculate monthly contribution
monthly_salary = (annual_salary / 12)

# Get % to save monthly
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
monthly_contribution = monthly_salary * portion_saved

# Get total cost of home
total_cost = float(input("Enter the cost of your dream home: "))

# Calculate how much down payment needed
needed_down_payment = total_cost * portion_down_payment

# While loop counter to add up all the contributions until target is achieved
n = 0
while current_savings < needed_down_payment:
    n = n + 1
    current_savings = (current_savings + (current_savings * r) + monthly_contribution)
    
# Return the answer
print(f"Number of months: {n}")
      
      

            
    
     

        