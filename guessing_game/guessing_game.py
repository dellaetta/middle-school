from datetime import date

while True:
    name = input("What is your name? ")
    year = input("What year were you born? ")
    place = input("Would you rather be on land or in the ocean? ")
    live = input("Do you like the city or the country better? ")
    food = input("One more question. What is your favorite food? ")
    birthYear = date.today().year - int(year)
    
    print()
    print(name,"you love the", live, "and", place,". You are also", birthYear, "years old and you like", food, "more than any other food.")
    print()

    if input("Press q (quit) or any other key to restart: ") == "q":
        break
    
