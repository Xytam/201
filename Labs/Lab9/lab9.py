def getSum(gradesList):
    sumValue = 0
    #loops over all values, incrementally adding each one
    for i in range(0,len(gradesList)):
        sumValue = sumValue + gradesList[i]
    return sumValue

def getAverage(gradesList):
    sumValue = getSum(gradesList)
    average = sumValue/len(gradesList)
    return average

def letterGrading(letterGrade):
    if(letterGrade>=90):
        return('A')
    elif(letterGrade>=80 and letterGrade<90):
        return('B')
    elif(letterGrade>=70 and letterGrade<80):
        return('C')
    elif(letterGrade>=60 and letterGrade<70):
        return('D')
    else:
        return('F')


filename="grades.txt"
f=open(filename,'r')

line1=f.readline()
line2=f.readline()
line3=f.readline()
line4=f.readline()
line1List=line1.split()
line2List=line2.split()
line3List=line3.split()
line4List=line4.split()
p1Grade=[]
p2Grade=[]
p3Grade=[]
p4Grade=[]
grade1=0
grade2=0
grade3=0
grade4=0
for i in range(1,len(line1List),2):
    p1Grade.append(float(line1List[i])*float(line1List[i+1]))
for i in range(1,len(line2List),2):
    p2Grade.append(float(line2List[i])*float(line2List[i+1]))
for i in range(1,len(line3List),2):
    p3Grade.append(float(line3List[i])*float(line3List[i+1]))
for i in range(1,len(line4List),2):
    p4Grade.append(float(line4List[i])*float(line4List[i+1]))
grade1=getSum(p1Grade)
grade2=getSum(p2Grade)
grade3=getSum(p3Grade)
grade4=getSum(p4Grade)
classGrades=[grade1,grade2,grade3,grade4]
classAverage=getAverage(classGrades)
l1=(str(line1List[0])+": "+str(round(grade1,2))+" - "+str(letterGrading(grade1)))
l2=(str(line2List[0])+": "+str(round(grade2,2))+" - "+str(letterGrading(grade2)))
l3=(str(line3List[0])+": "+str(round(grade3,2))+" - "+str(letterGrading(grade3)))
l4=(str(line4List[0])+": "+str(round(grade4,2))+" - "+str(letterGrading(grade4)))
l5=("Class average is: "+str(classAverage))

writeFile=open('grade_report.txt','w')
writeFile.write(l1+"\n")
writeFile.write(l2+"\n")
writeFile.write(l3+"\n")
writeFile.write(l4+"\n")
writeFile.write(l5+"\n")
