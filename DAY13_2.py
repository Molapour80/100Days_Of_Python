import json
import os
import random

# File paths
USERS_FILE = 'users.json'
FLASHCARDS_FILE = 'flashcards.json'

# Initialize data files
if not os.path.exists(USERS_FILE):
    with open(USERS_FILE, 'w') as f:
        json.dump({}, f)

if not os.path.exists(FLASHCARDS_FILE):
    with open(FLASHCARDS_FILE, 'w') as f:
        json.dump({}, f)

# User registration
def register(username, password):
    with open(USERS_FILE, 'r') as f:
        users = json.load(f)
    
    if username in users:
        return False  

    users[username] = password
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f)
    return True

# User login
def login(username, password):
    with open(USERS_FILE, 'r') as f:
        users = json.load(f)
    
    return users.get(username) == password

# Add flashcard
def add_flashcard(username, word, meaning):
    with open(FLASHCARDS_FILE, 'r') as f:
        flashcards = json.load(f)
    
    if username not in flashcards:
        flashcards[username] = []

    flashcards[username].append({'word': word, 'meaning': meaning})

    with open(FLASHCARDS_FILE, 'w') as f:
        json.dump(flashcards, f)

# View flashcards
def view_flashcards(username):
    with open(FLASHCARDS_FILE, 'r') as f:
        flashcards = json.load(f)

    return flashcards.get(username, [])

# Take quiz
def take_quiz(username):
    flashcards = view_flashcards(username)
    if not flashcards:
        return "No flashcards available for this user."

    card = random.choice(flashcards)
    answer = input(f"What is the meaning of '{card['word']}'? ")

    if answer.lower() == card['meaning'].lower():
        return "Correct!"
    else:
        return f"Wrong! The correct answer is '{card['meaning']}'."


# Main application flow
def main():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if register(username, password):
                print("Registration successful!")
            else:
                print("Username already exists.")

        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if login(username, password):
                print("Login successful!")
                while True:
                    print("\n1. Add Flashcard")
                    print("2. View Flashcards")
                    print("3. Take Quiz")
                    print("4. Logout")
                    option = input("Choose an option: ")

                    if option == '1':
                        word = input("Enter word: ")
                        meaning = input("Enter meaning: ")
                        add_flashcard(username, word, meaning)
                        print("Flashcard added!")

                    elif option == '2':
                        flashcards = view_flashcards(username)
                        if flashcards:
                            for card in flashcards:
                                print(f"{card['word']} - {card['meaning']}")
                        else:
                            print("No flashcards available.")

                    elif option == '3':
                        print(take_quiz(username))

                    elif option == '4':
                        print("Logged out.")
                        break

                    else:
                        print("Invalid option.")
            else:
                print("Invalid username or password.")

        elif choice == '3':
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()