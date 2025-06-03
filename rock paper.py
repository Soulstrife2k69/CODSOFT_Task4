import random

def get_computer_choice():
    # Randomly select rock, paper, or scissors
    return random.choice(["rock", "paper", "scissors"])

def get_user_choice():
    # Prompt the user until a valid choice is made
    while True:
        user_input = input("Choose rock, paper, or scissors: ").lower()
        if user_input in ["rock", "paper", "scissors"]:
            return user_input
        else:
            print("Invalid choice. Please enter rock, paper, or scissors.")

def decide_winner(user, computer):
    # Determine the game outcome
    if user == computer:
        return "tie"
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "scissors" and computer == "paper") or
        (user == "paper" and computer == "rock")
    ):
        return "user"
    else:
        return "computer"

def play_game():
    print("=== Rock-Paper-Scissors Game ===")
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = decide_winner(user_choice, computer_choice)

        if result == "tie":
            print("Result: It's a tie!")
        elif result == "user":
            print("Result: You win this round!")
            user_score += 1
        else:
            print("Result: Computer wins this round!")
            computer_score += 1

        # Show current scores
        print(f"\nScore => You: {user_score} | Computer: {computer_score}")

        # Ask if the user wants to play again
        again = input("\nDo you want to play another round? (yes/no): ").lower()
        if again != "yes":
            print("\nThanks for playing!")
            break

# Start the game
if __name__ == "__main__":
    play_game()

