print("Odd number Summation")

sum = 0

for hehe in range(0, 7, 1):
    numero = eval(input("Enter any number ---> "))
    if numero % 2:
        sum += numero
print("The sum of all given odd numbers is",sum)