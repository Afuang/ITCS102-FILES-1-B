print("Welcome to Mange Reccommender!")
print("Answer a few questions to find a new manga to read.")
print("Which Genre do you like to read?")
print("1.Shonen")
print("2.Romance")
print("3.Horror")
Genre_choice = input("Enter Choice (1,2,3): ")

if Genre_choice == "1":
    Genre = "Shonen"
    print("You selected: ",Genre)
    Duration = input("How long should the manga be? (Short, Medium ,Long) ")
    if Duration == "Short":
        y1 = input("What decade? (2000, 2010): ")
        if y1 == "2000":
            print("We recommend: Sand Land!")
        elif y1 == "2010":
            print("We recommend: D.Gray-man!")
    elif Duration == "Medium":
        y2 = input("What decade? (2000, 2010): ")
        if y2 == "2000":
            print("We recommend: Hunter x Hunter!")
        elif y2 == "2010":
            print("We recommend: Vampire Knight!")
    if Duration == "Long":
        y3 = input("What decade? (2000, 2010): ")
        if y3 == "2000":
            print("We recommend: One Piece!")
        elif y3 == "2010":
            print("We recommend: Fairy Tail!")

elif Genre_choice == "2":
    Genre = "Romance"
    print("You selected: ",Genre)
    Duration = input("How long should the manga be? (Short, Medium ,Long) ")
    if Duration == "Short":
        y1 = input("What decade? (2000, 2010): ")
        if y1 == "2000":
            print("We recommend: Skip Beat!")
        elif y1 == "2010":
            print("We recommend: Book Girl!")
    elif Duration == "Medium":
        y2 = input("What decade? (2000, 2010): ")
        if y2 == "2000":
            print("We recommend: Kare Kano!")
        elif y2 == "2010":
            print("We recommend: Love, Chunibyou & Other Delusions!")
    if Duration == "Long":
        y3 = input("What decade? (2000, 2010): ")
        if y3 == "2000":
            print("We recommend: Fruits basket!")
        elif y3 == "2010":
            print("We recommend: Nisekoi!")
elif Genre_choice == "3":
    Genre = "Horror"
    print("You selected: ",Genre)
    Duration = input("How long should the manga be? (Short, Medium ,Long) ")
    if Duration == "Short":
        y1 = input("What decade? (2000, 2010): ")
        if y1 == "2000":
            print("We recommend: Uzamaki!")
        elif y1 == "2010":
            print("We recommend: Hideout!")
    elif Duration == "Medium":
        y2 = input("What decade? (2000, 2010): ")
        if y2 == "2000":
            print("We recommend: Monster!")
        elif y2 == "2010":
            print("We recommend: Another!")
    if Duration == "Long":
        y3 = input("What decade? (2000, 2010): ")
        if y3 == "2000":
            print("We recommend: Homunculus!")
        elif y3 == "2010":
            print("Higurashi When They Cry!")




    
    
