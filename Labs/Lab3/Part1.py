temp = int(input("What is the temperature? "))
if(temp<25):
    print("It's freezing outside")
elif(temp>=25 and temp<50):
    print("It's a bit chilly, remember to bundle up")
elif(temp>=50 and temp<80):
    print("The weather is wonderful!")
elif(temp>=80 and temp<100):
    print("It's pretty hot outside!")
else:
    print("It's way too hot outside!")
