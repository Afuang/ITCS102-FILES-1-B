temp = eval(input("Enter temperature---> "))

if temp <= 0:
    print("The temperature is considered: below freezing")
elif temp >= 1 and temp <= 15:
    print("The temperature is considered: extremely cold")
elif temp >= 16 and temp <= 30:
    print("The temperature is considered: cold")
elif temp >= 31 and temp <= 45:
    print("The temperature is considered: lukewarm")
elif temp >= 46 and temp <= 60:
    print("The temperature is considered: extremely hot")
elif temp >= 61:
    print("The temperature is considered: burning")

else:
    print("invalid temperature")