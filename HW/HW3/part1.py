# File:    part1.py
# Author:  Jake Horvers
# Date:    9/22/09
# Section: 7
# E-mail:  horvers1@umbc.edu
# Description: Counts and replaces certain numbers
count=1
print("Greetings user! This program will count and replace numbers with words")
while(count<=100):
    #if divisible by both baz
    if(count%3==0 and count%5==0):
        print("baz")
        count+=1
    #divisible by 5 bar
    elif(count%5==0):
        print("bar")
        count+=1
    #divisible by 3 foo
    elif(count%3==0):
        print("foo")
        count+=1
    #Not divisible by anything? no prob, print the number
    else:
        print(count)
        count+=1
