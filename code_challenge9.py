print("🦜PARROT SIMULATOR -THE ECHO CHAMBER")
speak = input("What do you want your parrot to say? ")
rep = eval(input("How many times should the parrot squawk it? "))

print("Listen to your parrot:")

for i in range(1, rep, 1):
    print("🦜 Squawk!",speak)