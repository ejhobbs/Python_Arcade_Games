import random

print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down! Survive your")
print("desert trek and out run the natives.")

done = False
natives_travelled = -20
drinks_left = 5
miles_travelled = 0
camel_tiredness = 0
thirst = 0
while not done:
    #print choices
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")

    user_choice = input("Your Choice? ").lower()

    if user_choice == "q":
        done = True
    elif user_choice == "e":
        print("Miles travelled: ",miles_travelled)
        print("Drinks left: ",drinks_left)
        print("The natives are", miles_travelled-natives_travelled, "miles behind you")
    elif user_choice == "d":
        camel_tiredness = 0
        print("Camel is now happy!")
        natives_travelled += random.randrange(7,15)
    elif user_choice == "c":
        distance = random.randrange(10,21)
        miles_travelled += distance
        print("You travelled",distance,"miles")
        thirst += 1
        camel_tiredness += random.randrange(1,4)
        natives_travelled += random.randrange(7,15)
    elif user_choice == "b":
        distance = random.randrange(5,13)
        miles_travelled += distance
        print("You travelled",distance,"miles")
        thirst += 1
        camel_tiredness += 1
        natives_travelled += random.randrange(7,15)
    elif user_choice == "a":
        if drinks_left > 0:
            thirst -= 1
            drinks_left -= 1
            print("You take a drink")
        else:
            print("You have no drinks left!")

    # output conditions
    if random.random() < 0.05:
        print("You found an oasis!")
        drinks_left = 5
        thirst = 0
        camel_tiredness = 0
    if thirst > 6:
        print("You died of thirst!")
        done = True
    elif thirst > 4:
        print("You're thirsty!")

    if camel_tiredness > 8 and not done:
        print("Your camel died")
        done = True
    elif camel_tiredness > 5 and not done:
        print("Your camel is tired")

    if miles_travelled - natives_travelled <= 0 and not done:
        print("The natives have caught up with you!")
        done = True
    elif miles_travelled - natives_travelled < 15 and not done:
        print("The natives are getting close!")

    if miles_travelled >= 200 and not done:
        print("You escaped the desert!")
        done = True