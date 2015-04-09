def groupList(Ilist):
    highestNum=0
    count=0
    result=[]
    for i in range(0, len(Ilist)):
        if(Ilist[i]>highestNum):
            highestNum=Ilist[i]
        else:
            pass
    for i in range(0,highestNum+1):
        tempList=[]
        count=0
        for j in range(0,len(Ilist)-1):
            if(i==Ilist[j]):
                count+=1
            else:
                pass
        for m in range(0,count):
            tempList.append(i)
        if(count!=0):
           result.append(tempList)
        else:
           pass
    return result
def main():
    list1=[1,3,2,2,3,3,4,1]
    print(groupList(list1))

main()
