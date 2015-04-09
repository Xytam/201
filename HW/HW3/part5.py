# File:    part5.py
# Author:  Jake Horvers
# Date:    10/1/14
# Section: 7
# E-mail:  horvers1@umbc.edu
# Description: Detetmines modulus without division
print("Greetings user! This program will determine modulus")
a=int(input("Enter the first number: "))
b=int(input("Enter the number to mod it by: "))
#counts a as close to zero as possible
while(a>=0):
    #keep subtracting until there is nothing left
    if(a>=b):
       a= a-b
    #print leftover after you can't suybtract any more(modulus)
    else:
        print(a)
        a=-1
