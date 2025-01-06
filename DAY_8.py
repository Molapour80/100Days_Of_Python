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
    
def update(result):
    if not os.path.exists('score.txt'):
        with open('score.txt','w') as files:
            files.write("user_wins:0\ncomputer_wins:0\n")

    with open('score.txt', 'r') as files:
        scores = files.readlines()

    user_wins = int(scores[0].strip().split(':')[1])
    computer_wins = int(scores[1].strip().split(':')[1])

    if result == "You win:)":
        user_wins += 1
    elif result == "You lose :(!":
        computer_wins += 1

    with open('score.txt', 'w') as f:
        f.write(f"user_wins:{user_wins}\ncomputer_wins:{computer_wins}\n")

def display_scores():
    
    if os.path.exists('score.txt'):
        with open('score.txt', 'r') as files:
            scores = files.readlines()
        print("\nCurrent Scores:")
        print(f"You: {scores[0].strip().split(':')[1]} wins")
        print(f"Computer: {scores[1].strip().split(':')[1]} wins")
    else:
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
            
        update(result)
        display_scores()

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    main()

        
