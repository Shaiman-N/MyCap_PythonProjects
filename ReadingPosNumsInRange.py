# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 19:56:27 2023

@author: Aiman Sabah
"""

#Write a Python program to print all positive numbers in a range.
n=int(input("Enter the number of integers in a list : "))
print("Enter the ",n," number of integers in the list :\n")
nums=[]
for i in range(n):
    nums.append(int(input(str(i+1)+":")))
    
print("The input list of numbers is :\n")
print(nums)

pos=[]
for num in nums:
    if (str(num)).startswith("-")==False:
        pos.append(int(str(num)))

print("The list of positive numbers is : \n")        
print(pos)