
word = input("Enter a word:")
word_len = len(word)

number_list = []
total = 0

for i in range(1, word_len + 1, 1):
        number = int(input(f"Enter number {i}:"))
        total += number
        number_list.append(number)
print(number_list)
print(f"The length of the word is {word_len}")

def average_number():
    average = total / word_len
    print(f"The average of the numbers is {average}")
average_number()
def compare():
    average = total / word_len
    if average == i:
        print(f"The length of the word '{word}' is equal to the average.")
    elif average <= i:
        print(f"The length of the word '{word}' is less than the average.")
    elif average >= i:
        print(f"The length of the word '{word}' is greater than the average.")
compare()