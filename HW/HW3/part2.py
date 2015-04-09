# File:    part2.py
# Author:  Jake Horvers
# Date:    10/1/14
# Section: 7
# E-mail:  horvers1@umbc.edu
# Description: Determines primeness of a number

print("Greetings user! This program will determine if a number is prime")
input=int(input("Input a number to see if it is prime: "))
count=2
isprime='true'

#predetermines if number is 1 or 0, it's not prime as given, else continue
if(input==1 or input==0):
    isprime='false'
else:
    pass
#determines primeness by modulus operator, and testing divisibility
#by every number below it
while(count<input):
    if(input%count!=0):
        isprime='true'
    #escapes if it determines it's not prime
    elif(input%count==0):
        isprime='false'
        count=input
    else:
        pass
    count+=1

#prints result of primeness
if(isprime=='false'):
    print("Not Prime")
else:
    print("Prime")
