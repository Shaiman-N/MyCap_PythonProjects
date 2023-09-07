# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 18:52:44 2023

@author: Aiman Sabah
"""

#Write a Python program to print all positive numbers in a range.
nums=[]
x=map(int,input("enter a list of numbers separated with space :\n").strip().split())
nums+=x

print("The input list of numbers is :\n")
print(nums)

pos=[]
for num in nums:
    if (str(num)).startswith("-")==False:
        pos.append(int(str(num)))

print("The list of positive numbers is : \n")        
print(pos)