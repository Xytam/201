# File:    part4.py
# Author:  Jake Horvers
# Date:    10/1/14
# Section: 7
# E-mail:  horvers1@umbc.edu
# Description: Makes an asterisk triangle
print("Greetings user! This program will make an asterisk triangle")_
#input height
n=int(input("Please enter the height of your triangle: "))
k=1
s=0
while(k<=n):
    #prints the correct amount of stars
    if(s<k):
        print("*",end="")
        s+=1
    #goes to new line and resets after previous line
    else:
        print()
        s=0
        k+=1
