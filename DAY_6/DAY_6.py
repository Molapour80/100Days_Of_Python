import json
import os

NOTES_FILE = "notes.json"

#for read the notes in the json
def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, 'r') as file:
            return json.load(file)
    return []

#for write the note in the json
def save_notes(notes):
    with open(NOTES_FILE, 'w') as file:
        json.dump(notes, file)

#add note in notes.js
def add_note():
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    notes.append({"title": title, "content": content})
    save_notes(notes)
    print(f"Note '{title}' added.")

#display note 
def display_notes():
    if not notes:
        print("No notes available.")
    else:
        for index, note in enumerate(notes):
            print(f"{index + 1}. {note['title']}")

#Edite the note by index(id)
def edit_note():
    display_notes()
    if notes:
        note_id = int(input("Enter the note number to edit: ")) - 1
        if 0 <= note_id < len(notes):
            title = input("Enter new title: ")
            content = input("Enter new content: ")
            notes[note_id] = {"title": title, "content": content}
            save_notes(notes)
            print("Note updated.")
        else:
            print("Invalid note number.")

#Remove the note 
def remove_note():
    display_notes()
    if notes:
        note_id = int(input("Enter the note number to remove: ")) - 1
        if 0 <= note_id < len(notes):
            removed_note = notes.pop(note_id)
            save_notes(notes)
            print(f"Removed note: {removed_note['title']}")
        else:
            print("Invalid note number.")

# Main function :))))
notes = load_notes()

def main():

    try:
        while True:

            print("\n1. Add note")
            print("2. Display notes")
            print("3. Edit note")
            print("4. Remove note")
            print("5. Exit")
            
            choice = input("Choose an option: ")
            if choice == "1":
                add_note()
            elif choice == "2":
                display_notes()
            elif choice == "3":
                edit_note()
            elif choice == "4":
                remove_note()
            elif choice == "5":
                break
            else:
                print("Invalid choice.")
    except:
        print("Invalid function:((")


if __name__ == "__main__":
    main()