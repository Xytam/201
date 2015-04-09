#File: part1.py
#Author: Jake Horvers
#Date: 09/22/114
#Section: 4
#E-mail: horvers1@umbc.edu
#Description: Uses ifs and ors to determine generator status.

print("Greetings user... booting generator console...determining status...")
#Reads switch status
Switch1 = str(input("Switch number one (y/n): "))
Switch2 = str(input("Switch number two (y/n): "))
#Prints status
if((Switch1 == "y" and Switch2 == "y") or (Switch1 == "n" and Switch2 == "n")):
    print("The generator is off")
else:
    print("The generator is on")
