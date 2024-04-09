from replit import db
import random 

#Game
def game():
  print()
  print("Welcome to the game", username)
  print("Please enter a number between 1 and 10")
  number = int(input())
  if number < 1 or number > 10:
    print("Invalid number")
  else:
    print("You entered", number)
    print("The computer will now generate a random number")
    random_number = random.randint(1, 10)
    print("The random number is", random_number)
    if number == random_number:
      print("You win!")
    else:
      print("You lose!")
  print("\nPlay again? y/n")
  play_again = input()
  if play_again == "y":
    game()
  else:
    print("Thanks for playing!")
  

#main program
while True: 
  print()
  print("1. Add User")
  print("2. Login")
  print("3. Exit")
  choice = input("Enter your choice: ")
  if choice == "1":
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    while True: 
      salt = random.randint(1000,9999)
      newPassword = f"{password}{salt}"
      newPassword = hash(newPassword)
      db[username] = {"password": newPassword, "salt": salt}
      game()
      break
  elif choice == "2": 
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    salt = db[username]["salt"]
    oldPassword = f"{password}{salt}"
    oldPassword = hash(oldPassword)
    if oldPassword == db[username]["password"]:
      print("Login successful")
    else: 
      print("Login failed")
    
    db[username] = {"password": password, "score": 0}
    print("User added successfully!")

