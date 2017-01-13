score = 0

# Question One
print("Question One: \n"
      "What is 5*7")
answer = int(input("?: "))
if answer == 5*7:
    score += 1

# Question Two

print("Question Two: \n"
      "What is the chemical symbol for lead")
answer = input("?: ")
if answer == "Pb":
    score += 1

# Question 3

print("Question Three: \n"
      "Pigs can look up, true or false")
answer = input("?: ")
if answer.lower() == 'true':
    score += 1

# Finale

percentage = (100/3)*score
print("Congration, you done it\n"
      "You scored: ",score, ", Which is: ",percentage,"%")