for i in range(10):
    for j in range(10-i):
        print(" ", end = " ")
    for k in range(1,i+1):
        print(k, end = " ")
    for l in range(i-1,0,-1):
        print(l,end = " ")
    print()