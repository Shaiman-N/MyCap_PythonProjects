# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 20:26:14 2023

@author: Aiman Sabah
"""

"""
Write Python code to create a function called most_frequent that takes a string 
and prints the letters in decreasing order of frequency. Use dictionaries.

Your Input and output should look something like this

Input : Please enter a string Mississippi

Output : i = 04 s = 04 p =02 m =01
"""


def most_frequent(string):
    letter_dict={}
    for word in string:
        letters=word.split()
        for letter in letters:
            letter_dict[letter]=letter_dict.get(letter,0)+1
    
    letter_list=[]
    for key,val in letter_dict.items():
        letter_list.append((val,key))
    letter_list.sort(reverse=True)
    return(letter_list)

string=input("Please enter a string : ")
print("The letters of the string in decreasing order of frequency are : \n")
print(most_frequent(string))


