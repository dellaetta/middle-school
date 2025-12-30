
while(1):
  direction = input("Pick a direction (up, down, left, or right) or quit (q): ")

  if direction == "up":
    print("You are going to buy a bird.")

  elif direction == "down":
    print("You will not buy an pet.")

  elif direction == "right":
    print("You are going to buy a dog.")

  elif direction == "left":
    print("You will buy a cat.")
  
  elif direction == "q":
    print("Bye!")
    break

  else: 
    print("Not an option. Try again.")

