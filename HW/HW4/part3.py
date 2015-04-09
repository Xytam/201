# File:    part3.py
# Author:  Jake Horvers
# Date:    10/08/2014
# Section: 7
# E-mail:  horvers1@umbc.edu 
# Description:
# Adds elements of a 2 lists together

#Init  variables
list1=[]
list2=[]
list3=[]
keepReading='true'
#Read in list1
while(keepReading=='true'):
    num=str(input("Enter a number: "))
    if(num=='end'):
        keepReading='false'
    else:
        list1.append(int(num))
#Reset Boolean check variable
keepReading='true'
#Read in list2
while(keepReading=='true'):
    num=str(input("Enter a number: "))
    if(num=='end'):
        keepReading='false'
    else:
        list2.append(int(num))
#If list1 is bigger than list1, list3 becomes list1
#list3 is then added to list2 at each index
if(len(list1)>=len(list2)):
    list3=list1

   #Alternative readin
   # for i in range(0,len(list1)):
   #    list3.append(list1[i])

    for i in range(0,len(list2)):
        list3[i]+=list2[i]
#If list2 is bigger than list1 list3 becomes list2
#list3 is then added to list1 at each index
else:
    list3=list2

#    Alternative read in
#    for i in range(0,len(list2)):
#       list3.append(list2[i])

    for i in range(0,len(list1)):
        list3[i]+=list1[i]

print(list3)
