a1 = eval(input("Enter the amount to deposit : "))
m = a1
n1 = m // 1000
m = m % 1000
n2 = m // 500
m = m % 500
n3 = m // 200
m = m % 200
n4 = m //100
m = m % 100
n5 = m // 50
m = m % 50
n6 = m // 20
m = m % 20
n7 = m // 10
m = m % 10
n8 = m // 5
m = m % 5
n9 = m // 1
m = m % 1
print("Here is a breakdown of the deposited ammount : ")
print("1000 = ",n1)
print("500 = ",n2)
print("200 = ",n3)
print("100 = ",n4)
print("50 = ",n5)
print("20 = ",n6)
print("10 = ",n7)
print("5 = ",n8)
print("1 = ",n9)


