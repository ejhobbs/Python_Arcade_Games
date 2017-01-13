import random

user_choice = input("Rock, Paper, Scissors?: ").lower()
cpu_choice = random.randrange(0,3)
if cpu_choice == 0:
    cpu_choice = "rock"
elif cpu_choice == 1:
    cpu_choice = "paper"
else:
    cpu_choice = "scissors"

if cpu_choice == user_choice:
    print("Draw!")
elif user_choice == "rock":
    if cpu_choice == "scissors":
        print("I win")
    elif cpu_choice == "paper":
        print("You win")
elif user_choice == "paper":
    if cpu_choice == "scissors":
        print("You win")
    elif cpu_choice == "rock":
        print("I win")
elif user_choice == "scissors":
    if cpu_choice == "rock":
        print("You win")
    elif cpu_choice == "paper":
        print("I win")
else:
    print("I don't recognise that move..")