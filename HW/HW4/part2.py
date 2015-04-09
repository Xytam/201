# File:    part2.py
# Author:  Jake Horvers
# Date:    10/08/2014
# Section: 7
# E-mail:  horvers1@umbc.edu 
# Description:
# Inputs numbers on a list and determines longest run

myList=[]
isANumber='true'
run=1
runCompare=1
while(isANumber=='true'):
    myNum=str(input("Please enter a number: "))
    myList.append(myNum)
    if(myList[len(myList)-1]=='end'):
        isANumber='false'
    else:
        pass
myList.sort()
for i in range(0,len(myList)-1):
    if(myList[i]==myList[i+1]):
        run+=1
        if(run>runCompare):
            runCompare=run+1
        else:
            pass
    else:
        run=0
print("Your largest run was: ", runCompare)
