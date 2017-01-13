count_positive = 0
count_negative = 0
count_zero = 0

for i in range(7):
    num = float(input("Pls give me a number: "))
    if num > 0:
        count_positive += 1
    elif num == 0:
        count_zero += 1
    else:
        count_negative += 1

print("Number of Positive: ", count_positive)
print("Number of Zero: ", count_zero)
print("Numer of Negative: ", count_negative)