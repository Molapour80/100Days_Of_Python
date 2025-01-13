import random
word =["python", "programming", "challenge", "keyboard", "computer", "hangman", "development"]
chosen = random.choice(word)
guessed_letters = [] 
attemp = 6

print("Welcome to the word guessing game!")
print("You have to guess the word. You can guess one letter at a time.")
print("_ " * len(chosen))
while attemp > 0:
    guses = input("Enter your geeses:").lower()
    
    if guses == guessed_letters:
        print("You already guessed that letter. Try again.")
        continue
    guessed_letters.append(guses)

    if guses in chosen:
        print("Good job! You guessed a letter!")
    else:
        attemp += 1

    current_word_display = ''.join([letter if letter in guessed_letters else '_' for letter in chosen])
    print("Current word: " + ' '.join(current_word_display))

    if '_' not in current_word_display:
        print("Congratulations! You've guessed the word:", chosen)
        break
else:
    print("You've run out of attempts! The word was:", chosen)



