import random

def get_user_choice():
    choices = {'1': 'rock', '2': 'paper', '3': 'scissors'}
    user_choice = ''
    while user_choice not in choices:
        user_choice = input("Choose 1 (rock), 2 (paper), or 3 (scissors): ")
        if user_choice not in choices:
            print("Invalid choice! Please try again.")
    return choices[user_choice]

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "win"
    else:
        return "lose"

def display_result(user_choice, computer_choice, result):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if result == "tie":
        print("It's a tie!")
    elif result == "win":
        print("You win!")
    else:
        print("You lose!")

def play_again():
    while True:
        again = input("Do you want to play again? (y/n): ").lower()
        if again in ['y', 'n']:
            return again == 'y'
        print("Invalid input! Please enter 'y' or 'n'.")

def play_game():
    user_score = 0
    computer_score = 0
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, result)

        if result == "win":
            user_score += 1
        elif result == "lose":
            computer_score += 1

        print(f"\nScore: You {user_score} - Computer {computer_score}")

        if not play_again():
            break

    print("\nFinal Score:")
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")
    print("Thanks for playing!")

# Call the play_game function to start the game
play_game()
