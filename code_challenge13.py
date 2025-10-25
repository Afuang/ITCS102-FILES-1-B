pangalan = input("What is your name?  ")
print("Welcome to odd number summation", pangalan)
print("#########################################")
gumagamit = ""
kabuuan = 0
lahat = ""
while gumagamit != 0:
    gumagamit = eval(input("\nInsert the number---> "))
    check = gumagamit % 2
    if check == 1:
        print("Your number is a odd number, continue coding....")
        kabuuan += gumagamit
        gumagamit = str(gumagamit)
        lahat += gumagamit + " "
    elif check == 0:
        print("Your number is a even number, continue coding....")
print("The number inserted is not countable, coding stops....")
print("\n",pangalan, "The total summation of the odd numbers has a total of ",kabuuan)
print("These is the total of number inserted ",lahat)
