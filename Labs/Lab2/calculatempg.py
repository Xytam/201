#File: MPGCalculator
#Written by: Jake Horvers
#Date: 9/16/14
#Section:
#Email: horvers1@umbc.edu
#Description: Calculate miles per gallon given distance and gallons used.
distanceTraveled=int(input('Enter distance traveled: '))
gallonsUsed=int(input('Enter gallons Used: '))
MPG= (distanceTraveled/gallonsUsed)
print('The MPG is: ', MPG)
