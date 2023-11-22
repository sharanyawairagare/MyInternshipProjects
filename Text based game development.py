import time

# Define game functions

def intro():
    print("Welcome to the Text Adventure Game!")
    time.sleep(1)
    print("You find yourself in a mysterious place...")
    time.sleep(1)
    print("You have to make some choices to find your way out.")
    time.sleep(1)
    start_game()

def start_game():
    print("\nYou encounter a fork in the road.")
    print("Do you want to go left or right?")

    choice = input("Enter your choice (left/right): ").lower()

    if choice == "left":
        go_left()
    elif choice == "right":
        go_right()
    else:
        print("Invalid choice. Try again.")
        start_game()

def go_left():
    print("\nYou chose to go left.")
    time.sleep(1)
    print("You find a key! This might be useful later.")
    time.sleep(1)
    print("You encounter a locked door.")
    time.sleep(1)
    print("Do you want to use the key to unlock the door?")
    
    use_key = input("Enter 'yes' or 'no': ").lower()

    if use_key == "yes":
        print("\nThe door unlocks! You proceed to the next room.")
        next_room()
    elif use_key == "no":
        print("\nYou decide not to use the key.")
        next_room()
    else:
        print("Invalid choice. Try again.")
        go_left()

def go_right():
    print("\nYou chose to go right.")
    time.sleep(1)
    print("You encounter a trap!")
    time.sleep(1)
    print("You narrowly avoid it and proceed to the next room.")
    next_room()

def next_room():
    print("\nYou enter a room with three chests.")
    time.sleep(1)
    print("Which chest do you want to open? (1, 2, or 3)")

    chest_choice = input("Enter your choice: ")

    if chest_choice == "1":
        print("\nYou found a map! It reveals the way out.")
        game_over("You found the exit!")
    elif chest_choice == "2":
        print("\nA monster jumps out! You are eaten. Game over.")
        game_over("You lost!")
    elif chest_choice == "3":
        print("\nYou found a hidden passage. You escape!")
        game_over("You win!")
    else:
        print("Invalid choice. Try again.")
        next_room()

def game_over(message):
    print("\n--- Game Over ---")
    print(message)
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        intro()
    else:
        print("Thanks for playing!")

# Start the game
intro()