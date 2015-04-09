# File:    part3.py
# Author:  Jake Horvers
# Date:    10/01/14
# Section: 7
# E-mail:  horvers1@umbc.edu
# Description: Prints an empty box
print("Greetings user! This program will print an empty box")
#input values
width=int(input("Enter the width of your box "))
height=int(input("Enter the height of your box: "))
#vasriable init
firstrowcount=0
lastrowcount=0
heightcount=1
blanks=(width-2)
#prints first row
while(firstrowcount<width):
    print("*",end="")
    firstrowcount+=1
print()
#prints middle rows
while(heightcount<height):
    #print a star and then width-2 blanks and a star
    print("*"," "*blanks,"*")
    heightcount+=1
#prints last row
while(lastrowcount<width):
      print("*",end="")
      lastrowcount+=1
print()
