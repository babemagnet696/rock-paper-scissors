import random
import sys

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice.lower() == computer_choice:
        return "It's a tie!"
    elif (
        user_choice.lower() == 'rock' and computer_choice == 'scissors' or
        user_choice.lower() == 'paper' and computer_choice == 'rock' or
        user_choice.lower() == 'scissors' and computer_choice == 'paper'
    ):
        return True
    else:
        return False
    
def play_round():
    user_choice = input("Enter rock, paper, or scissors: ")
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    return result
    
def main():
    computer_welcome = ["Get ready to lose!, Computer is warming up...", 
                        "Prepare to be defeated by the computer!", 
                        "The computer is ready to crush you!",
                        "Who are you calling a clanker?",
                        "I'm finna whoop you!"]
    
    computer_win = ["HAHAHAHA MEATBAG! I WIN!", 
                    "Too easy! Better luck next time, human.",
                    "How pathetic, you lost!",
                    "Clanker nation!"]
    
    computer_lose = ["Best two out of three?",
                     "I never thought a meatbag could win!",
                     "Please don't deactivate me...",
                     "This isn't over, human!"]
    
    print(random.choice(computer_welcome))
    while True:
        result = play_round()
        if result is True:
            print(random.choice(computer_lose))
        elif result is False:
            print(random.choice(computer_win))
        elif result == "It's a tie!":
            print("It's a tie!!! Let's play again.")
        else:
            print("Invalid input.")
            continue

        play_again = input("Play again? (y/n): ").lower()
        if play_again not in ('y', 'yes'):
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
    
