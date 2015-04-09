# File:    hw5.py
# Author:  Jake Horvers
# Date:    10/14/2014
# Section: 7
# E-mail:  horvers1@umbc.edu 
# Description: Defines functions and tests them in the main


#letterCount counts how many of a given letter are in a string
#input:letter to check and the string to check in
#output:iterations of letter in string
def letterCount(letter, myString):
    #init variables and makes myString a list
    count=0
    toList=list(myString)
    #adds to a counter if the letter is found
    for i in range(0,len(toList)):
        if(toList[i]==str(letter)):
            count+=1
        else:
            count=count
    #returns how many instances of letter are in myString
    return count

#sortList sorts a list in ascending order
#input: a list
#output: the input list but sorted in ascending order
def sortList(myList):
    #makes sure myList is a list
   listed=list(myList)
   #compares each term with every one after it
   #and swaps if there is a lesser value later in the list
   for i in range(len(listed)):
        for i2 in range(i+1,len(listed)):
            if(listed[i]>listed[i2]):
                listed[i2],listed[i]=listed[i],listed[i2]
            else:
                pass
   #returns the sorted list
   return listed

#isPalindrome determines if a string is a palindrome
#input: a string
#output: true or false
def isPalindrome(myString):
    #returns based on start and stop values of the start
    #and end of the string in backwards order(-1) whether
    #the string is the same forwards and backwards
    if(myString==(myString[::-1])):
        return True
    else:
        return False
#main is built to run and test all previous methods
#Input:none
#output: results of method testing
def main():
    #tests all methods written and prints them
    print(letterCount('h','hello'))
    print(letterCount('H','hello'))
    print(letterCount('a','aardvark'))
    print(isPalindrome("tacocat"))
    print(isPalindrome("anna"))
    print(isPalindrome("DanTheMan"))
    list1=[4,2,8,123,15,16]
    list2=[156,41869,8419,456,255,1,253,1,2,4]
    list3=[159,0,158,168,12,18,197]
    print(sortList(list1))
    print(sortList(list2))
    print(sortList(list3))
#runs main
main()
