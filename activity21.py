cleaning = True
sum = 0
while cleaning == True:
    confirm = input("Do you want to continue cleaning it? ( y / n )").lower()
    sum += 1
    if confirm == 'y':
        print('Cleaning continues....')
        continue
    else:
        print('Cleaning stops.....')
        break

print(f'the total clenings is {sum}')