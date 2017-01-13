import random

count_heads = 0;
count_tails = 0;

for i in range(50):
    result = random.randrange(0,2)
    if result == 1:
        print("heads")
        count_heads += 1
    else:
        print("tails")
        count_tails += 1

print("Number of heads: ",count_heads)
print("Number of tails: ",count_tails)