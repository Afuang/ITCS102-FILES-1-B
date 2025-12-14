import os
import time
user = input("What is your name---> ")
os.system('cls')
print("SYNCHRONIZING.......")
time.sleep(0.5)
os.system('cls')
print("WELCOME",user,"TO BASICS OF PYTHON")
print("Choose what lesson do you want to learn")


while True:
    print("A - PRINT STATEMENTS")
    print("B - VARIABLES")
    print("C - OPERATORS")
    print("D - LOOPS")
    print("E - LISTING")
    print("F - FUNCTIONS")
    print("G = USE NOTEPAD")
    print("H - EXIT THE MENU")

    choice = input("SELECT FROM THE CHOICES ABOVE ---> ").lower()
    os.system('cls')
    print("SYNCHRONIZING.......")
    os.system('cls')
    if choice == 'a':
        os.system('cls')
        while True:
            print("CHOOSE WHAT TO DO---> ")
            print("A = DEFINITION")
            print("B = OUTPUT EXAMPLE")
            print("C = GO BACK TO MAIN MENU")
            choice_a = input("SELECT FROM THE OPTIONS ABOVE---> ").lower()
            print("SYNCHRONIZING.......")
            time.sleep(0.5)
            os.system('cls')
            if choice_a =='a':
                print("A print statement in programming refers to a command or function used to display information to the user or an output device, typically the console or terminal. Its primary purpose is to output data, which can include text messages, the values of variables, or the results of computations, during program execution.")
                print("\nHere are examples of how to write different types of print statements:")
                print("\nprint(\"HELLO WORLD\")")
                back = input("DO YOU WANT TO CONTINUE (y/n)---> ").lower()
                if back == 'n':
                    print("SYNCHRONIZING.......")
                    time.sleep(0.5)
                    os.system('cls')
                    break
                elif back == 'y':
                    print("SYNCHRONIZING.......")
                    time.sleep(0.5)
                    os.system('cls')
                    continue
                else:
                    print("INVALID RESPONSE PLS TRY AGAIN")
                    time.sleep(0.5)
                    os.system('cls')
                    continue
            elif choice_a =='b':
                print("SYNCHRONIZING.......")
                time.sleep(0.5)
                os.system('cls')
                example = input("ENTER ANY WORDS YOU WANT TO PRINT---> ")
                print("SYNCHRONIZING.......")
                time.sleep(0.5)
                os.system('cls')
                print(example)
                back = input("DO YOU WANT TO CONTINUE (y/n)---> ").lower()
                if back == 'n':
                    print("SYNCHRONIZING.......")
                    time.sleep(0.5)
                    os.system('cls')
                    break
                elif back == 'y':
                    print("SYNCHRONIZING.......")
                    os.system('cls')
                    time.sleep(0.5)
                    continue
                else:
                    print("INVALID RESPONSE PLS TRY AGAIN")
                    time.sleep(0.5)
                    os.system('cls')
                    continue
            elif choice_a == 'c':
                print("SYNCHRONIZING.......")
                time.sleep(0.5)
                os.system('cls')
                break
            else:
                print("INVALID RESPONSE PLS TRY AGAIN")
                time.sleep(1)
                os.system('cls')
                continue
    elif choice == 'b':
        os.system('cls')
        while True:
            print("CHOOSE WHAT TO DO---> ")
            print("A = DEFINITION")
            print("B = EXAMPLE")
            print("C = GO BACK TO MAIN MENU")
            choice_a = input("SELECT FROM THE OPTIONS ABOVE---> ").lower()
            print("SYNCHRONIZING.......")
            time.sleep(0.5)
            os.system('cls')
            if choice_a =='a':
                print("a variable is a symbolic name that refers to a location in computer memory where a value can be stored. It acts as a container or a label for a piece of data within a program.")
                print("\nHere are examples of how to write different types of variable statements:")
                print("\nADRIAN = POGI")
                print("name = input(\"ENTER YOUR NAME\")")
                print("print(\"pogi si\",name,)")
                back = input("DO YOU WANT TO CONTINUE (y/n)---> ").lower()
                if back == 'n':
                    print("SYNCHRONIZING.......")
                    time.sleep(0.5)
                    os.system('cls')
                    break
                elif back == 'y':
                    print("SYNCHRONIZING.......")
                    time.sleep(0.5)
                    os.system('cls')
                    continue
                else:
                    print("INVALID RESPONSE PLS TRY AGAIN")
                    time.sleep(0.5)
                    os.system('cls')
                    continue
            elif choice_a =='b':
                print("SYNCHRONIZING.......")
                time.sleep(0.5)
                os.system('cls')
                fname = input("ENTER YOUR FIRST NAME----> ").upper()
                mname = input("ENTER YOUR MIDDLE INITIAL---> ").upper()
                lname = input("ENTER YOUR LAST NAME---> ").upper()
                age = input("ENTER YOUR AGE---> ")
                print("SYNCHRONIZING.......")
                time.sleep(0.5)
                os.system('cls')
                
                print(F"MY NAME IS {fname} {mname}. {lname} IM {age} YEARS OLD")
                back = input("DO YOU WANT TO CONTINUE (y/n)---> ").lower()
                if back == 'n':
                    print("SYNCHRONIZING.......")
                    time.sleep(0.5)
                    os.system('cls')
                    break
                elif back == 'y':
                    print("SYNCHRONIZING.......")
                    os.system('cls')
                    time.sleep(0.5)
                    continue
                else:
                    print("INVALID RESPONSE PLS TRY AGAIN")
                    time.sleep(0.5)
                    os.system('cls')
                    continue
            elif choice_a == 'c':
                print("SYNCHRONIZING.......")
                time.sleep(0.5)
                os.system('cls')
                break
            else:
                print("INVALID RESPONSE PLS TRY AGAIN")
                time.sleep(1)
                os.system('cls')
                continue
    elif choice == 'c':
        os.system('cls')
        while True:
            print("CHOOSE WHAT TO DO---> ")
            print("A = DEFINITION")
            print("B = EXAMPLE")
            print("C = GO BACK TO MAIN MENU")
            choice_a = input("SELECT FROM THE OPTIONS ABOVE---> ").lower()
            print("SYNCHRONIZING.......")
            time.sleep(0.5)
            os.system('cls')
            if choice_a =='a':
                print("Programming operators are symbols that perform actions on variables/values (operands), primarily categorized as Arithmetic (+, -, *, /), Assignment (=, +=), Comparison/Relational (==, >, <), Logical (&&, ||, !), Bitwise (&, |),")
                print("\nHere are examples of how to write different types of Arithmetic & Assignment operators:")
                print("ARITHMETIC OPERATORS")
                print("n1 = input(\"ENTER THE 1ST NUMBER---> \")")
                print("n2 = input(\"ENTER THE 2ND NUMBER---> \")")
                print("\nAddition = n1 + n2")
                print("Substraction = n1 - n2")
                print("Multiplication = n1 * n2")
                print("Divition = n1 / n2")
                print("print(\"ADDITION\")")
                print("print(\"SUBSTRACTION)")
                print("print(\"MULTIPLICATION\")")
                print("print(\"DIVITION\")")
                print("\nASSIGNMENT OPERATORS")
                print("\nn1 = n2")
                print("n1 += n2")
                back = input("DO YOU WANT TO CONTINUE (y/n)---> ").lower()
                if back == 'n':
                    print("SYNCHRONIZING.......")
                    time.sleep(0.5)
                    os.system('cls')
                    break
                elif back == 'y':
                    print("SYNCHRONIZING.......")
                    time.sleep(0.5)
                    os.system('cls')
                    continue
                else:
                    print("INVALID RESPONSE PLS TRY AGAIN")
                    time.sleep(0.5)
                    os.system('cls')
                    continue
            elif choice_a =='b':
                print("SYNCHRONIZING.......")
                time.sleep(0.5)
                os.system('cls')
                print("WELCOME TO BASIC CALCULATOR")
                print("IM GOING TO SHOW YOU THE USE OF ARITHMETIC OPERATORS AND ASSIGNMENT OPERATORS AS CALCULATOR")
                while True:
                    print("A = ADDITION")
                    print("B = SUBSTRACTION")
                    print("C = MULTIPLICATION")
                    print("D = DIVITION")
                    choice_c = input("PICK FROM THE CHOICES ABOVE---> ").lower()
                    if choice_c == 'a':
                        print("ADDITION PLS INPUT ANY NUMBER")
                        num1 = eval(input("ENTER THE FIRST NUMBER---> "))
                        num2 = eval(input("ENTER THE SECOND NUMBER---> "))
                        print("SYNCHRONIZING.......")
                        time.sleep(0.5)
                        os.system('cls')
                        a = num1 + num2
                        print(num1,"+",num2,"=",a)
                        break
                    elif choice_c == 'b':
                        print("SUBSTRACTION PLS INPUT ANY NUMBER")
                        num1 = eval(input("ENTER THE FIRST NUMBER---> "))
                        num2 = eval(input("ENTER THE SECOND NUMBER---> "))
                        print("SYNCHRONIZING.......")
                        time.sleep(0.5)
                        os.system('cls')
                        a = num1 - num2
                        print(num1,"-",num2,"=",a)
                        break
                    elif choice_c == 'c':
                        print("MULTIPLICATION PLS ANY NUMBER")
                        num1 = eval(input("ENTER THE FIRST NUMBER---> "))
                        num2 = eval(input("ENTER THE SECOND NUMBER---> "))
                        print("SYNCHRONIZING.......")
                        time.sleep(0.5)
                        os.system('cls')
                        a = num1 * num2
                        print(num1,"x",num2,"=",a)
                        break
                    elif choice_c == 'd':
                        print("DIVITION PLS INPUT ANY NUMBER")
                        num1 = eval(input("ENTER THE FIRST NUMBER---> "))
                        num2 = eval(input("ENTER THE SECOND NUMBER---> "))
                        print("SYNCHRONIZING.......")
                        time.sleep(0.5)
                        os.system('cls')
                        a = num1 / num2
                        print(num1,"%",num2,"=",a)
                        break
                    else:
                        print("INVALID RESPONSE PLS TRY AGAIN")
                        time.sleep(1)
                        os.system('cls')
                        continue
                back = input("DO YOU WANT TO CONTINUE (y/n)---> ").lower()
                if back == 'n':
                    print("SYNCHRONIZING.......")
                    time.sleep(0.5)
                    os.system('cls')
                    break
                elif back == 'y':
                    print("SYNCHRONIZING.......")
                    os.system('cls')
                    time.sleep(0.5)
                    continue
                else:
                    print("INVALID RESPONSE PLS TRY AGAIN")
                    time.sleep(0.5)
                    os.system('cls')
                    continue
            elif choice_a == 'c':
                print("SYNCHRONIZING.......")
                time.sleep(0.5)
                os.system('cls')
                break
            else:
                print("INVALID RESPONSE PLS TRY AGAIN")
                time.sleep(1)
                os.system('cls')
                continue
    elif choice == 'd':
        os.system('cls')
        while True:
            print("CHOOSE WHAT TO DO---> ")
            print("A = DEFINITION")
            print("B = EXAMPLE")
            print("C = GO BACK TO MAIN MENU")
            choice_a = input("SELECT FROM THE OPTIONS ABOVE---> ").lower()
            print("SYNCHRONIZING.......")
            time.sleep(0.5)
            os.system('cls')
            if choice_a =='a':
                print("a loop is a control structure that repeats a block of code multiple times until a specific condition is met, saving programmers from writing repetitive code and making programs more efficient and concise. Loops work by checking a condition, executing the code if true, and then re-checking until the condition becomes false, at which point the program exits the loop. Common types include for loops (for known iterations) and while/do-while loops (for condition-based repetition).")
                print("\nHere are examples of how to write for loop & while loop statements")
                print("\nFOR LOOP STATEMENT")
                print("for i in range(1, 20, 1):")
                print("print(i,\"boom\")")
                print("\nWHILE LOOP STATEMENT")
                print("while True:")
                print("\bcounter = input(\"this question will not stop unless you input stop---> \")")
                print("if counter == 'stop':")
                print("thank you for stopping the question")
                print("break")
                print("else:")
                print("ok questioning continues.......")
                print("continue")
                back = input("DO YOU WANT TO CONTINUE (y/n)---> ").lower()
                if back == 'n':
                    print("SYNCHRONIZING.......")
                    time.sleep(0.5)
                    os.system('cls')
                    break
                elif back == 'y':
                    print("SYNCHRONIZING.......")
                    time.sleep(0.5)
                    os.system('cls')
                    continue
                else:
                    print("INVALID RESPONSE PLS TRY AGAIN")
                    time.sleep(0.5)
                    os.system('cls')
                    continue
            elif choice_a =='b':
                print("SYNCHRONIZING.......")
                time.sleep(0.5)
                os.system('cls')
                print("IM GOING TO SHOW YOU THE TWO DIFERENT TYPES OF LOOPS FOR LOOP, AND WHILE LOOP")
                print("A = FOR LOOP")
                print("B = WHILE LOOP")
                choice_d = input("PLEASE CHOOSE WHAT TYPE OF LOOP DO YOU WANT TO USE---> ").lower()

                if choice_d == 'a':
                    print("🦜PARROT SIMULATOR -THE ECHO CHAMBER")
                    speak = input("What do you want your parrot to say? ")
                    rep = eval(input("How many times should the parrot squawk it? "))
                    print("Listen to your parrot:")

                    for i in range(1, 1+rep, 1):
                        print("🦜 Squawk!",speak)
                        time.sleep(0.3)
                elif choice_d == 'b':
                    print("WELCOME TO MANG INASAL UNLI RICE SIMULATOR")
                    while True:
                        rice = input("SIR DO YOU WANT MORE RICE (y/n)---> ").lower()
                        if rice == 'y':
                            print("SERVING RICE.......")
                            time.sleep(1)
                            print("HERE YOU GO SIR")
                            os.system('cls')
                            continue
                        elif rice == 'n':
                            time.sleep(1)
                            print("SIR JUST CALL ME IF YOU WANT MORE RICE")
                            os.system('cls')
                            break
                        else:
                            print("INVALID RESPONSE PLS TRY AGAIN")
                            time.sleep(1)
                            os.system('cls')
                            continue
    

                back = input("DO YOU WANT TO CONTINUE (y/n)---> ").lower()
                if back == 'n':
                    print("SYNCHRONIZING.......")
                    time.sleep(0.5)
                    os.system('cls')
                    break
                elif back == 'y':
                    print("SYNCHRONIZING.......")
                    os.system('cls')
                    time.sleep(0.5)
                    continue
                else:
                    print("INVALID RESPONSE PLS TRY AGAIN")
                    time.sleep(0.5)
                    os.system('cls')
                    continue
            elif choice_a == 'c':
                print("SYNCHRONIZING.......")
                time.sleep(0.5)
                os.system('cls')
                break
            else:
                print("INVALID RESPONSE PLS TRY AGAIN")
                time.sleep(1)
                os.system('cls')
                continue
    elif choice == 'e':
        os.system('cls')
        while True:
            print("CHOOSE WHAT TO DO---> ")
            print("A = DEFINITION")
            print("B = EXAMPLE")
            print("C = GO BACK TO MAIN MENU")
            choice_a = input("SELECT FROM THE OPTIONS ABOVE---> ").lower()
            print("SYNCHRONIZING.......")
            time.sleep(0.5)
            os.system('cls')
            if choice_a =='a':
                print("A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements. Each element or value that is inside of a list is called an item. Just as strings are defined as characters between quotes, lists are defined by having values between square brackets [ ] .")
                print("\nHere are examples of how to create and use lists in Python statements:")
                print("\ngrocery = ['sardinas', 'meat loaf', 'gatas', 'instant noodles']")
                print("grocery.append(\"tinapay\")")
                print("grocery.insert(3,\"asukal\")")
                print("grocery.pop()")
                print("grocery.remove('sardinas')")
                print("grocery.sort")
                print("print(grocery)")
                back = input("DO YOU WANT TO CONTINUE (y/n)---> ").lower()
                if back == 'n':
                    print("SYNCHRONIZING.......")
                    time.sleep(0.5)
                    os.system('cls')
                    break
                elif back == 'y':
                    print("SYNCHRONIZING.......")
                    time.sleep(0.5)
                    os.system('cls')
                    continue
                else:
                    print("INVALID RESPONSE PLS TRY AGAIN")
                    time.sleep(0.5)
                    os.system('cls')
                    continue
            elif choice_a =='b':
                print("SYNCHRONIZING.......")
                time.sleep(0.5)
                os.system('cls')
                print("WELCOME TO LISTING SIMULATOR")
                any_list = [ ]
             
                while True:
                    list = input("INPUT YOU WANT TO ADD ON YOUR LIST(ENTER YOU WANT TO ADD / STOP)---> ").lower()
                    if list == 'stop':
                        print("LISTING COMPLETED")
                        print("HERE IS THE RESULT")
                        break
                    else:
                        any_list.append(list)
                        print(list,"IS ADDED TO YOUR LIST, LISTING CONTINUES.......")
                        continue
                print("THIS IS ALL THAT YOU INPUT ON YOUR LIST")
                for list in any_list:
                    print(f"YOU GOT---> {list} ")
                back = input("DO YOU WANT TO CONTINUE (y/n)---> ").lower()
                if back == 'n':
                    print("SYNCHRONIZING.......")
                    time.sleep(0.5)
                    os.system('cls')
                    break
                elif back == 'y':
                    print("SYNCHRONIZING.......")
                    os.system('cls')
                    time.sleep(0.5)
                    continue
                else:
                    print("INVALID RESPONSE PLS TRY AGAIN")
                    time.sleep(0.5)
                    os.system('cls')
                    continue
            elif choice_a == 'c':
                print("SYNCHRONIZING.......")
                time.sleep(0.5)
                os.system('cls')
                break
            else:
                print("INVALID RESPONSE PLS TRY AGAIN")
                time.sleep(1)
                os.system('cls')
                continue
    elif choice == 'f':
        os.system('cls')
        while True:
            print("CHOOSE WHAT TO DO---> ")
            print("A = DEFINITION")
            print("B = OUTPUT EXAMPLE")
            print("C = GO BACK TO MAIN MENU")
            choice_a = input("SELECT FROM THE OPTIONS ABOVE---> ").lower()
            print("SYNCHRONIZING.......")
            time.sleep(0.5)
            os.system('cls')
            if choice_a =='a':
                print("a function is a named, reusable block of code that performs a specific task only when it is called. Functions allow programmers to break down complex problems into smaller, manageable chunks, which makes code more organized, readable, testable, and efficient")
                print("\nHere are examples of common Python statements used inside a function:")
                print("def greeting(name):")
                print("\bprint(\"hello\",name,\")")
                print("\bname = 'Adrian'")
                back = input("DO YOU WANT TO CONTINUE (y/n)---> ").lower()
                if back == 'n':
                    print("SYNCHRONIZING.......")
                    time.sleep(0.5)
                    os.system('cls')
                    break
                elif back == 'y':
                    print("SYNCHRONIZING.......")
                    time.sleep(0.5)
                    os.system('cls')
                    continue
                else:
                    print("INVALID RESPONSE PLS TRY AGAIN")
                    time.sleep(0.5)
                    os.system('cls')
                    continue
            elif choice_a =='b':
                print("SYNCHRONIZING.......")
                time.sleep(0.5)
                os.system('cls')
                def greet_user(name):
                    print(f"Hello, {name}!")
                greet_user('Adrian')
                back = input("DO YOU WANT TO CONTINUE (y/n)---> ").lower()
                if back == 'n':
                    print("SYNCHRONIZING.......")
                    time.sleep(0.5)
                    os.system('cls')
                    break
                elif back == 'y':
                    print("SYNCHRONIZING.......")
                    os.system('cls')
                    time.sleep(0.5)
                    continue
                else:
                    print("INVALID RESPONSE PLS TRY AGAIN")
                    time.sleep(0.5)
                    os.system('cls')
                    continue
            elif choice_a == 'c':
                print("SYNCHRONIZING.......")
                time.sleep(0.5)
                os.system('cls')
                break
            else:
                print("INVALID RESPONSE PLS TRY AGAIN")
                time.sleep(1)
                os.system('cls')
                continue

    elif choice == 'g':

        while True:
            print("NOW TRY CREATING YOUR OWN CODE")
            print("CHOOSE FROM THE OPTION BELOW")
            print("A = USE NOTEPAD")
            print("B = TRY THE OUTPUT")
            print("C = GO BACK TO MENU")
            testing = input("CHOOSE FROM THE OPTION ABOVE---> ").lower()
            if testing == 'a':
                print("LOADING.......")
                time.sleep(0.5)
                os.system('cls')
                os.system('type nul > testing_area')
                os.system('notepad testing_area')
                continue
            elif testing == 'b':
                print("LOADING.......")
                time.sleep(0.5)
                os.system('cls')
                os.system('python testing_area')
                continue
            elif testing == 'c':
                print("LOADING.......")
                time.sleep(0.5)
                os.system('cls')
                break
            else:
                print("LOADING.......")
                time.sleep(0.5)
                os.system('cls')
                print("INVALID RESPONSE PLS TRY AGAIN")
                continue

    elif choice == 'h':
        print("SYNCHRONIZING.......")
        time.sleep(0.5)
        os.system('cls')
        print(f"THANK YOU {user} FOR USING THIS PROGRAM")
        break
    else:
        print("INVALID RESPONSE PLS TRY AGAIN")
        time.sleep(1)
        os.system('cls')
        continue
    