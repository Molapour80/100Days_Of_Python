import random

word = ["python", "programming", "challenge", "keyboard", "computer", "hangman", "development"]

# Function to set difficulty
def set_difficulty():
    print("Choose a difficulty level:")
    print("1. Easy (10 attempts)")
    print("2. Medium (6 attempts)")
    print("3. Hard (4 attempts)")
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        return 10
    elif choice == '2':
        return 6
    elif choice == '3':
        return 4
    else:
        print("Invalid choice. Defaulting to Medium (6 attempts).")
        return 6

chosen = random.choice(word)
guessed_letters = [] 
attempts = set_difficulty()

print("Welcome to the word guessing game!")
print("You have to guess the word. You can guess one letter at a time.")
print("_ " * len(chosen))

while attempts > 0:
    guess = input("Enter your guess: ").lower()
    
    if guess in guessed_letters:
        print("You already guessed that letter. Try again.")
        continue
    guessed_letters.append(guess)

    if guess in chosen:
        print("Good job! You guessed a letter!")
    else:
        attempts -= 1  # Decrease attempts on wrong guess

    current_word_display = ''.join([letter if letter in guessed_letters else '_' for letter in chosen])
    print("Current word: " + ' '.join(current_word_display))
    print(f"Attempts remaining: {attempts}")

    if '_' not in current_word_display:
        print("Congratulations! You've guessed the word:", chosen)
        break
else:
    print("You've run out of attempts! The word was:", chosen)