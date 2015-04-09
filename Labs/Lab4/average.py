amount=int(input("How many numbers do you want to average?: "))
count=0
total=0
while(count<amount):
    given=int(input("Enter the next number: "))
    total+=given
    count+=1
print((total/amount)," is the average of your numbers")
