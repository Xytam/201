import random

randnum = random.randint(1,10)

choice='y'
guess=0
print("Guess a number between 1 and 10 (inclusive) and I'll tell you if you're right!")
while(guess!=randnum and choice=='y'):
          guess=int(input("Enter your guess: "))
          if(guess==randnum):
                    print("You win.")
          else:
                    choice=str(input("WRONG! Would you like to play again?: "))
