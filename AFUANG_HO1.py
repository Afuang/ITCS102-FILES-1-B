word = input("Enter a word:")
word_len = len(word)
number_list = [ ]
total = 0
for i in range(1,1+word_len,1):
    number = eval(input(f"Enter number {i}:"))
    total += number
    number_list.append(number)
average = total / i
print(number_list)
print(f"The length of the word is {i}")
print(f"The average of the numbers is {average}")
if average == i:
    print(f"The length of the word '{word}' is equal the average.")
elif average >= i:
    print(f"The length of the word '{word}' is greater than the average.")
elif average <= i:
    print(f"The length of the word '{word}' is less than the average.")