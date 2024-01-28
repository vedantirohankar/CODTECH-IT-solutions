# Print a welcome message
print("Welcome to the Haunted House Part1!!")
print("One upon a time a man living in that house is passed way,with a strange incident and now nobody leaves there house is totaaly empty")
print("You with your college friend came for a jungle trip and you found that Haunted House")
print("The house is Fullly of dusty , all around the messy . You walk in the front door.")
print("Do you want to enter the Haunted house room1 or  room2 ?")

# Prompt user for a choice
chooseroom = input("> ")

if(chooseroom == "room1"):
  print("You enter the room1.")
  print("As you walk in, you see a sleeping monster there behind the diamonds.")
  print("Do you want to steal the diamonds ?")

  diamonds = input("> ")

  if(diamonds == "yes"):
    print("You attempt to steal the diamonds, but the monster wakes up and rips you into shreds.")
    print("You are now dead.")
  elif(diamonds == "no"):
    print("You decide to not steal the diamonds.")
    print("You turn around and leave the house safely.")
  else:
    print("Invalid choice. Please enter yes or no.")
elif(chooseroom == "Room2"):
  print("You chose to go into the Room2.")
  print("As you walk in, you see a Old shiny box lightning around the whole room.")
  print("Do you want to open the Box?")

  boxChoice = input("> ")

  if(boxChoice == "yes"):
    print("You open the box and it was full of snakes around the box")
  elif(boxChoice == "no"):
    print("You decide not to open the lightning Box.")
    print("As you turn to leave, you hear a cracking sound coming from the corner and someone catches you.")
    print("You unfortunaletly dead")
    print("You wake up in your bed. It was all a dream.")
  else:
    print("Invalid choice. Please enter yes or no.")
else:
  print("Invalid choice. Please enter room1 or room2.")