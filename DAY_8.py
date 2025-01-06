##Game
import random
import os
def get_user():

    choice = input("choice the one of them 'rock' ,'paper' or Scissors :").lower()
    while choice not in ["rock", "paper", "scissors"]:
        choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()
    return choice

def get_cumputer():

     return random.choice(["rock", "paper", "scissors"])

def winner_game(user_choice,computer_choice):

    if user_choice == computer_choice:
        return "It's a tie-.-!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win:)"
    else:
        return "You lose :(!"
    
def update_scores(winner):
    """Update the scores based on the winner."""
    scores = {"user_wins": 0, "computer_wins": 0}

    
    try:
        with open('scores.txt', 'r') as f:
            for line in f:
                key, value = line.strip().split(':')
                scores[key] = int(value)
    except FileNotFoundError:
        pass

    if winner == "You win:)":
        scores["user_wins"] += 1
    elif winner == "You lose :(!":
        scores["computer_wins"] += 1

    
    with open('scores.txt', 'w') as f:
        for key, value in scores.items():
            f.write(f"{key}:{value}\n")

def display_scores():
    
    try:
        with open('scores.txt', 'r') as f:
            scores = f.readlines()
            print("\nCurrent Scores:")
            for line in scores:
                print(line.strip())
    except FileNotFoundError:
        print("No scores available.")
    
def main():
    print("Welcome to Rock, Paper, Scissors *_*")
    while True:
        user_choice= get_user()

        computer_choice = get_cumputer()

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
            
        result = winner_game(user_choice, computer_choice)
        print(result)
        update_scores(result)
        
        display_scores()
        

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    main()

        
