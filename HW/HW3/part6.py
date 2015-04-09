# File:    part6.py
# Author:  Jake Horvers
# Date:    10/1/14
# Section: 7
# E-mail:  horvers1@umbc.edu
# Description: Forces a user to enter a positive number
print("Greetings user! This program will force you to enter a positive number")
positiveCheck='false'
while(positiveCheck=='false'):
    number=int(input("Please enter a positive number: "))
    #checks if the number is greater than 0
    if(number>0):
        print("Your number was: ",number)
        positiveCheck='true'
    else:
        pass
