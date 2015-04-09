def findNumInList(myList,num):
    for i in range (0,len(myList)):
        if(myList[i] == num):
            print("Found number: %d" %num)
        else:
            pass

def main():
    myList = [1,25,7,99,12]

    #Gets number from user, and appends it to the existing list
    num = int(input("Enter a number to be added to the end of the list: "))
    myList.append(num)
    findNumInList(myList,num)
main()
