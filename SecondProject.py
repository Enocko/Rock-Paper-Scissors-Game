import random

def get_user_choice():
    while True:
        user_input = input("Choose: 0 for Rock, 1 for Paper, 2 for Scissors: ")
        if user_input not in ["0", "1", "2"]:
            print("Invalid choice. Please choose 0, 1, or 2.")
        else:
            return int(user_input)

def get_computer_choice():
    return random.randint(0, 2)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a draw"
    elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
        return "You win!"
    else:
        return "Computer wins!"

def game():
    user_win = 0
    computer_win = 0
    options = ['Rock', 'Paper', 'Scissors']

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose {options[user_choice]}, and the computer chose {options[computer_choice]}.")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_win += 1
        elif result == "Computer wins!":
            computer_win += 1

        play_again = input("Would you like to play again? Type 'y' to continue or 'q' to quit: ").lower()
        if play_again == 'q':
            break
        

    print("Final Scores:")
    print("You won", user_win, "times")
    print("Computer won", computer_win, "times")
    print("Goodbye!")

game()
