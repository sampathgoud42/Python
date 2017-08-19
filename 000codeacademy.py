# Script Name	: 000_code_academy.py
# Author		: Sampath Kumar
# Created		: 6th August 2017
# Last Modified	: 
# Version		: 1.0

# Modifications	:

# Description	: This is practice session from code academy.
""" String always in double quotes """
my_name = "Sampath"
""" Boolean can be True or False"""
am_i_robo= False
am_i_human = True

meal = 44.50
tax = 6.75 / 100
tip = 15.0 / 100

meal = meal + meal * tax
total = meal + meal * tip

""" This will print upto 2 decimals of float variable total """
print("%.2f" % total)

"""Escaping characters using forward slash \ """
'It\'s me'

""" access by index """
a = "Apple"[0]
print (a)  
""" In Python3 use the parenthesis to print value"""
"""Strings and methods """
parrot = "Norwegian Blue"
pi = 3.14
print (len(parrot))
print (parrot.lower())
print (parrot.upper())
""" str(number) Converts number to String eg 3.14 to "3.14" """
print (str(pi))
""" String Concatenation"""
print ("Spam "+ "and "+ "eggs")
"""The % operator after a string is used to combine a string with variables. """
name = input("What is your name? ")
quest = input("What is your quest? ")
color = input("What is your favorite color? ")
""" String formatting with % """
print ("Ah, so your name is %s, your question is %s, " \
       "and your favorite color is %s."  %(name, quest, color))


my_string = "Sampath is at Ecole cafe"
print (len(my_string))
print (my_string.upper())






