#File: part1.py
#Author: Jake Horvers
#Date: 09/22/114
#Section: 4
#E-mail: horvers1@umbc.edu
#Description: Uses if/else input to diagnose

print("Hello User! This program is designed to dianose how horribly sick you are!")

#If the user has a fever, continues to ask questions
fever = str(input("Do you have a fever? (y/n): "))
if(fever == ("y")):
   rash = str(input("Do you have a rash? (y/n): "))

   #Prints measles diagnosis
   if(fever == ("y") and rash == ("y")):
      print("Diagnosis: Measles")

   #If there's no rash, asks about ears
   elif(fever == ("y") and rash == ("n")):
       ear = str(input("Do your ears hurt? (y/n): "))

      #Determines Ear infection or flu
       if(ear == ("y")):
          print("Diagnosis: Ear Infection")

       else:
          print("Diagnosis: Flu")

   else:
      print("Invalid response...")


#If the user doesn't have a fever, asks about nose
else:
   nose = str(input("Do you have a stuffy nose? (y/n): "))
   if(fever == ("n") and nose == ("n")):
       print("Diagnosis: Hypochondriac")

   elif(fever == ("n") and nose == ("y")):
       print("Diagnosis: Head Cold")





