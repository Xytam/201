# File:    hw7.py
# Author:  Jake Horvers
# Date:    11/6/2014
# Section: 7
# E-mail:  horvers1@umbc.edu 
# Description:
#Converts input text file to base 10 and then to another base the user
#specifies and saves it to a new file

#
print("This is a filter program that will convert your text file into ASCII values...")
#Reads in file and assigns it's contents to contents var
fileName=str(input("Enter the name of the file: "))
readFile=open(fileName,'r')
contents=readFile.read()
#Ensures the base is valid(betwen 2 and 9 inclusive)
validBase=False
while(validBase==False):
    base=input("Enter a base between 2 and 9: ")
    isValidBase=False
    try:
        int(base)
        isValidBase= True
    except ValueError:
        isValidBase= False
    if(isValidBase==True):
        base=int(base)
        if(isValidBase==True and base>=2 and base<=9):
            validBase=True
        else:
            validBase=False
    else:
        isValidBase=False
    
#Init new contents to be sent to output file
replacementContents=""
base10=0

#goes through every point in contents
for i in range (0,len(contents)):
    #adds a new line every 5 values
    if(i%5==0):
        replacementContents+='\n'
    else:
        pass
    #Checks alphanumerical status
    if(contents[i].isalpha()==False):
        replacementContents+=" .. "
    else:
        #Converts letter to ascii base 10
        base10=ord(contents[i])
        baseNumber=0
        #converts base 10 to given base
        while(base10>0):
            if((base10-pow(base,8))>=0):
                base10-=(pow(base,8))
                baseNumber+=100000000
            elif((base10-pow(base,7))>=0):
                base10-=(pow(base,7))
                baseNumber+=10000000
            elif((base10-pow(base,6))>=0):
                base10-=(pow(base,6))
                baseNumber+=1000000
            elif((base10-pow(base,5))>=0):
                base10-=(pow(base,5))
                baseNumber+=100000
            elif((base10-pow(base,4))>=0):
                base10-=(pow(base,4))
                baseNumber+=10000
            elif((base10-pow(base,3))>=0):
                base10-=(pow(base,3))
                baseNumber+=1000
            elif((base10-pow(base,2))>=0):
                base10-=(pow(base,2))
                baseNumber+=100
            elif((base10-pow(base,1))>=0):
                base10-=(pow(base,1))
                baseNumber+=10
            elif((base10-pow(base,0))>=0):
                base10-=(pow(base,0))
                baseNumber+=1
            else:
                pass
        #adds converted base number to contents
        replacementContents+=str(baseNumber)
        replacementContents+=" "

#creates and writes to new file
newFileName=str(str(base)+'_'+str(fileName))
writeFile=open(newFileName,"w")
writeFile.write(replacementContents)
print("To read the new file contents type: cat ",newFileName)

#closes both files
writeFile.close()
readFile.close()
