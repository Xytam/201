# File:    part1.py
# Author:  Jake Horvers
# Date:    10/08/2014
# Section: 7
# E-mail:  horvers1@umbc.edu 
# Description:
# Takes 2 numbers as input and makes a square of numbers
width=int(input("Input the width: "))
height=int(input("Input the height: "))
num=1
counter=1
heightcounter=1
while(heightcounter<=height):
    counter=1
    while(counter<=width):
        print(num,end="")
        counter+=1
        num+=1
    print()
    heightcounter+=1
