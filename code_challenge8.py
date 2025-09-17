print("MULTIPLICATION TABLE MAKER")

NUM = eval(input("Enter a number: "))

for i in range(1, 11, 1):
    result = NUM * i
    print(NUM, "x",i,"=",result)