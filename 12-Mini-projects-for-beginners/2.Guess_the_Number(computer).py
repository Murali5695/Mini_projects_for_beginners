import random

def guess(x):
    random_number=random.randint(1,x)
    #print(random_number)
    guess_number=0
    while random_number!=guess_number:
        guess_number = int(input(f"Enter the number between 1 to {x}:"))
        if guess_number>random_number:
            print("Sorry Try Again. you guess the number Too High..:( ")
        elif guess_number<random_number:
            print("Sorry Try Again. you guess to number Too low...:( ")

    print(f"Congrats you guess the correct number. the Number is {random_number}")

x=int(input("Enter the range:"))
guess(x)