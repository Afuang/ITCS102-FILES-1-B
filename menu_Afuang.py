import os
import time
user = input("What is your name---> ")
os.system('cls')
print("LOADING.......")
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
    print("G - EXIT THE MENU")

    choice = input("SELECT FROM THE CHOICES ABOVE ---> ").lower()
    os.system('cls')
    print("LOADING.......")
    os.system('cls')
    if choice == 'a':
        os.system('cls')
        while True:
            print("CHOOSE WHAT TO DO---> ")
            print("A = DEFINITION")
            print("B = EXAMPLE")
            print("C = GO BACK TO MAIN MENU")
            choice_a = input("SELECT FROM THE OPTIONS ABOVE---> ").lower()
            print("LOADING.......")
            time.sleep(0.5)
            os.system('cls')
            if choice_a =='a':
                print("A print statement in programming refers to a command or function used to display information to the user or an output device, typically the console or terminal. Its primary purpose is to output data, which can include text messages, the values of variables, or the results of computations, during program execution.")
                back = input("DO YOU WANT TO CONTINUE (y/n)---> ").lower()
                if back == 'n':
                    print("LOADING.......")
                    time.sleep(0.5)
                    os.system('cls')
                    break
                elif back == 'y':
                    print("LOADING.......")
                    time.sleep(0.5)
                    os.system('cls')
                    continue
                else:
                    print("INVALID RESPONSE PLS TRY AGAIN")
                    time.sleep(0.5)
                    os.system('cls')
                    continue
            elif choice_a =='b':
                print("LOADING.......")
                time.sleep(0.5)
                os.system('cls')
                example = input("ENTER ANY WORDS YOU WANT TO PRINT---> ")
                print("LOADING.......")
                time.sleep(0.5)
                os.system('cls')
                print(example)
                back = input("DO YOU WANT TO CONTINUE (y/n)---> ").lower()
                if back == 'n':
                    print("LOADING.......")
                    time.sleep(0.5)
                    os.system('cls')
                    break
                elif back == 'y':
                    print("LOADING.......")
                    os.system('cls')
                    time.sleep(0.5)
                    continue
                else:
                    print("INVALID RESPONSE PLS TRY AGAIN")
                    time.sleep(0.5)
                    os.system('cls')
                    continue
            elif choice_a == 'c':
                print("LOADING")
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
            print("LOADING.......")
            time.sleep(0.5)
            os.system('cls')
            if choice_a =='a':
                print("a variable is a symbolic name that refers to a location in computer memory where a value can be stored. It acts as a container or a label for a piece of data within a program.")
                back = input("DO YOU WANT TO CONTINUE (y/n)---> ").lower()
                if back == 'n':
                    print("LOADING.......")
                    time.sleep(0.5)
                    os.system('cls')
                    break
                elif back == 'y':
                    print("LOADING.......")
                    time.sleep(0.5)
                    os.system('cls')
                    continue
                else:
                    print("INVALID RESPONSE PLS TRY AGAIN")
                    time.sleep(0.5)
                    os.system('cls')
                    continue
            elif choice_a =='b':
                print("LOADING.......")
                time.sleep(0.5)
                os.system('cls')
                fname = input("ENTER YOUR FIRST NAME----> ").upper()
                mname = input("ENTER YOUR MIDDLE INITIAL---> ").upper()
                lname = input("ENTER YOUR LAST NAME---> ").upper()
                age = input("ENTER YOUR AGE---> ")
                print("LOADING.......")
                time.sleep(0.5)
                os.system('cls')
                
                print(F"MY NAME IS {fname} {mname}. {lname} IM {age} YEARS OLD")
                back = input("DO YOU WANT TO CONTINUE (y/n)---> ").lower()
                if back == 'n':
                    print("LOADING.......")
                    time.sleep(0.5)
                    os.system('cls')
                    break
                elif back == 'y':
                    print("LOADING.......")
                    os.system('cls')
                    time.sleep(0.5)
                    continue
                else:
                    print("INVALID RESPONSE PLS TRY AGAIN")
                    time.sleep(0.5)
                    os.system('cls')
                    continue
            elif choice_a == 'c':
                print("LOADING")
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
            print("LOADING.......")
            time.sleep(0.5)
            os.system('cls')
            if choice_a =='a':
                print("Programming operators are symbols that perform actions on variables/values (operands), primarily categorized as Arithmetic (+, -, *, /), Assignment (=, +=), Comparison/Relational (==, >, <), Logical (&&, ||, !), Bitwise (&, |),")
                back = input("DO YOU WANT TO CONTINUE (y/n)---> ").lower()
                if back == 'n':
                    print("LOADING.......")
                    time.sleep(0.5)
                    os.system('cls')
                    break
                elif back == 'y':
                    print("LOADING.......")
                    time.sleep(0.5)
                    os.system('cls')
                    continue
                else:
                    print("INVALID RESPONSE PLS TRY AGAIN")
                    time.sleep(0.5)
                    os.system('cls')
                    continue
            elif choice_a =='b':
                print("LOADING.......")
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
                        print("LOADING.......")
                        time.sleep(0.5)
                        os.system('cls')
                        a = num1 + num2
                        print(num1,"+",num2,"=",a)
                        break
                    elif choice_c == 'b':
                        print("SUBSTRACTION PLS INPUT ANY NUMBER")
                        num1 = eval(input("ENTER THE FIRST NUMBER---> "))
                        num2 = eval(input("ENTER THE SECOND NUMBER---> "))
                        print("LOADING.......")
                        time.sleep(0.5)
                        os.system('cls')
                        a = num1 - num2
                        print(num1,"-",num2,"=",a)
                        break
                    elif choice_c == 'c':
                        print("MULTIPLICATION PLS ANY NUMBER")
                        num1 = eval(input("ENTER THE FIRST NUMBER---> "))
                        num2 = eval(input("ENTER THE SECOND NUMBER---> "))
                        print("LOADING.......")
                        time.sleep(0.5)
                        os.system('cls')
                        a = num1 * num2
                        print(num1,"x",num2,"=",a)
                        break
                    elif choice_c == 'd':
                        print("DIVITION PLS INPUT ANY NUMBER")
                        num1 = eval(input("ENTER THE FIRST NUMBER---> "))
                        num2 = eval(input("ENTER THE SECOND NUMBER---> "))
                        print("LOADING.......")
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
                    print("LOADING.......")
                    time.sleep(0.5)
                    os.system('cls')
                    break
                elif back == 'y':
                    print("LOADING.......")
                    os.system('cls')
                    time.sleep(0.5)
                    continue
                else:
                    print("INVALID RESPONSE PLS TRY AGAIN")
                    time.sleep(0.5)
                    os.system('cls')
                    continue
            elif choice_a == 'c':
                print("LOADING")
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
            print("LOADING.......")
            time.sleep(0.5)
            os.system('cls')
            if choice_a =='a':
                print("a loop is a control structure that repeats a block of code multiple times until a specific condition is met, saving programmers from writing repetitive code and making programs more efficient and concise. Loops work by checking a condition, executing the code if true, and then re-checking until the condition becomes false, at which point the program exits the loop. Common types include for loops (for known iterations) and while/do-while loops (for condition-based repetition).")
                back = input("DO YOU WANT TO CONTINUE (y/n)---> ").lower()
                if back == 'n':
                    print("LOADING.......")
                    time.sleep(0.5)
                    os.system('cls')
                    break
                elif back == 'y':
                    print("LOADING.......")
                    time.sleep(0.5)
                    os.system('cls')
                    continue
                else:
                    print("INVALID RESPONSE PLS TRY AGAIN")
                    time.sleep(0.5)
                    os.system('cls')
                    continue
            elif choice_a =='b':
                print("LOADING.......")
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
                        rice = input("SIR DO YOU WANT MORE RICE (y/n)---> ")
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
                    print("LOADING.......")
                    time.sleep(0.5)
                    os.system('cls')
                    break
                elif back == 'y':
                    print("LOADING.......")
                    os.system('cls')
                    time.sleep(0.5)
                    continue
                else:
                    print("INVALID RESPONSE PLS TRY AGAIN")
                    time.sleep(0.5)
                    os.system('cls')
                    continue
            elif choice_a == 'c':
                print("LOADING")
                time.sleep(0.5)
                os.system('cls')
                break
            else:
                print("INVALID RESPONSE PLS TRY AGAIN")
                time.sleep(1)
                os.system('cls')
                continue


    elif choice == 'g':
        print("LOADING.......")
        time.sleep(0.5)
        os.system('cls')
        print("THANK YOU FOR USING THIS PROGRAM")
        break
    else:
        print("INVALID RESPONSE PLS TRY AGAIN")
        time.sleep(1)
        os.system('cls')
        continue
    