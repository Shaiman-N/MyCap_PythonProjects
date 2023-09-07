# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 21:32:41 2023

@author: Aiman Sabah
"""

n=int(input("Enter the required length of the fibonacci sequence: "))
t1=0
t2=1
print("The first %d numbers of the fibonacci series are: %d\t%d"%(n,t1,t2),end="\t")
nt=2
while(nt<n):
    t3=t1+t2
    print(t3,end="\t")
    t1=t2
    t2=t3
    nt+=1
    