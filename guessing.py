import random

numbers=[1,2,3,4,5,6,7,8,9]
guess=input("your guess : ")
randomNumber=random.choice(numbers)

if randomNumber==guess:
    print("you win")
else:
    print("you lose")
    print("the number is : ")
    print(randomNumber)