listy=[]
intmax=0
keepReading='true'
while(keepReading=='true'):
    num=str(input("Enter a number or q to find the max of the list: "))
    if(num=='q'):
        keepReading='false'
    else:
        listy.append(num)
for i in range(0,len(listy)):
    if(int(listy[i])>=intmax):
           intmax=int(listy[i])
    else:
           pass
print(intmax," is the max.")
