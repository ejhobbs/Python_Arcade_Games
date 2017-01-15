for i in range(10,-1,-1):
    for k in range(10-i):
        print(" ", end = " ")
    for j in range(i-1):
        print(j, end = " ")
    print()