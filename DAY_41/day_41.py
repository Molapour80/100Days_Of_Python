import random

def hangman():
    words = ['python', 'programming', 'computer', 'algorithm', 'developer']
    word = random.choice(words).lower()
    guessed_letters = []
    tries = 6  
    
    print("Welcome to Hangman!")
    print("_ " * len(word))
    
    while tries > 0:
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter!")
            continue
            
        if guess in guessed_letters:
            print("You've already guessed that letter!")
            continue
            
        guessed_letters.append(guess)
        
        if guess in word:
            print("Correct!")
        else:
            tries -= 1
            print(f"Wrong! You have {tries} tries left.")
            
       
        display = []
        for letter in word:
            if letter in guessed_letters:
                display.append(letter)
            else:
                display.append("_")
        print(" ".join(display))
        
    
        if "_" not in display:
            print("Congratulations! You won!")
            return
            
    print(f"You lost! The word was: {word}")

hangman()