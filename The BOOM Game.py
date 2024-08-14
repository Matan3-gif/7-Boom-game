# Check if the number is divisible by 7
def check_boom(number):
    return number % 7 == 0

def play_game(start_player):
    player = start_player.capitalize()  # Capitalize the starting player's name
    current_number = 1  # Start the game at 1

    while current_number <= 100:  # Loop until  100
        if player == "User":  # If it's the user's turn
            user_input = input(f"{player}: ")  # Ask user for input

            if user_input.lower() == 'boom':  # If user says "boom"
                if not check_boom(current_number):  # Check if its the correct time for "boom"
                    print("Game over")  # Incorrect use of "boom", game over
                    break
            else:
                try:
                    user_number = int(user_input)
                    if user_number != current_number:  # Check if user entered the correct number
                        print("Game over")
                        break
                except ValueError:
                    print("Error. Try again.")  # Non-numeric input, ask user to try again
                    continue

        else:  # If its the computer's turn
            if check_boom(current_number):  # Check if its the correct time for "boom"
                print(f"{player}: Boom")
            else:
                print(f"{player}: {current_number}")  # Print the current number

        current_number += 1  # Increment of 1 each loop
        player = "Computer" if player == "User" else "User"  # Switch to the other player

def start_game():
    while True:
        choice = input("Who would you like to start? Enter 'user' or 'computer': ")
        if choice == 'user' or choice == 'computer':
            play_game(choice)  # Starts game with the chosen player
            play_again = input("Do you want to play again? (yes/no): ")
            if play_again != "yes":
                break
        else:
            print("Invalid choice. Please try again.")

start_game()
