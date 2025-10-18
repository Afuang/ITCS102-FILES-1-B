
for i in range(1, 11, 1):
    for j in range(11, i, -1):
        print(" ",end = " ")
    for b in range(1, i-1, 1):
        print("&",end = " ")
    for l in range(1, i, 1):
        print("&",end = " ")
    print()