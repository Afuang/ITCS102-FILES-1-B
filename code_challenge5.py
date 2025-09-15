print("THE FACTORIAL PROGRAM")

numero = eval(input("Enter any number ---> "))
factor = 1
for b in range(numero, 0, -1):
    factor *= b
print("The factorial of",numero,"is",factor)