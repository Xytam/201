#File: part2.py
#Author: Jake Horvers
#Date: 09/22/114
#Section: 4
#E-mail: horvers1@umbc.edu
#Description: Calculates a grade based on weights.

print("Hello user! This program is designed to calculate your grade...")
#Get Values
HWWeight = float(input("Homework weight: "))
HWGrade = int(input("Homework grade: "))
ExamWeight = float(input("Exam weight: "))
ExamGrade = int(input("Exam grade: "))
DiscWeight = float(input("Discussion weight: "))
DiscGrade = int(input("Discussion grade: "))

#Determine grade

StudentGrade = ((HWWeight*HWGrade)+(ExamWeight*ExamGrade)+(DiscWeight*DiscGrade))

#Print Grade
if (StudentGrade >= 90):
    print("Student's grade is an A")
elif (StudentGrade >= 80 and StudentGrade < 90):
    print ("Student's grade is a B")
elif (StudentGrade >= 70 and StudentGrade < 80):
    print ("Student's grade is a C")
elif (StudentGrade >= 60 and StudentGrade < 70):
    print ("Student's grade is a D")
elif (StudentGrade < 60):
    print ("Student's grade is an F")
else:
    print("Invalid Grade...")

