name = input("What is your name ? ---> ")
bayad = eval(input("Fare fee ---> "))
studyante = input("Are you currently a student (yes / no) ")

if studyante == 'yes':
	discount = bayad * 0.2
	#bayad -= discount
	new_bayad = bayad - discount
	print("Hi ", name)
	print("Your Discount is ", discount)
	print("Your new fare is ", new_bayad)
else:
	print("Sorry ", name, "You are not eligible for a student discount")