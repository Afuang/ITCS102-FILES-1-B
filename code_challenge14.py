name = input("Enter your name---> ")
print("Welcome to anime listing" ,name)
listing_anime = [ ]

while True:
    anime = input("Enter the anime that you want to put (enter any anime / stop)").lower()
    
    if anime == 'stop':
        print("Listing is over here is the result ")
        break
        
    else:
        listing_anime.append(anime)
        print(anime, "Is added, listing continues....")
        continue
    
print("This is all the anime you listed ",anime)
for anime in listing_anime:
    print(f"You got---> {anime} ")