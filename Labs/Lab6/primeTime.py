def isPrime(myNum):
    count=2
    while(count<myNum):
        if(myNum%count!=0):
            count+=1
        else:
            return False
    return True
def getPrimes(myNum):
    primeList=[]
    for i in range(2,myNum):
        if(isPrime(i)):
            primeList.append(i)
        else:
            pass
    return primeList
def main():
    number=int(input("Please enter a number: "))
    print(getPrimes(number))
main()
