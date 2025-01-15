#TO_DO_LIST
import json
import os
import datetime
"""Create the file for save the information tasks"""
FILENAME = 'tasks.json'

def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(FILENAME, 'w') as file:
        json.dump(tasks, file)

def main():
    tasks = load_tasks()

    while True:
        print("\nWelcom to to do list")
        print("1.Add the task")
        print("2.Delete the task")
        print("3.update task")
        print("4.View the task")
        print("5.Exit")

        try :
            print("choes the option")
            choes = input("Enter your choese:")
                
            if choes in "1":
                task = input("Enter your task:")
                if task not in  tasks:
                    tasks.append(task)
                    save_tasks(tasks)
                    print("ADDED!!!")
                return f"Not add the task{task}"
                
            elif choes in "2":
                task = input("Enter the task you want to delete:")
                if task in tasks:
                    tasks.remove(task)
                    save_tasks(task)
                    print("Removed!!")
                return f"Task is not exsist the tasks{task}"

            elif choes in "3":
                    
                task = input("Enter the task you want to update:")
                if task in tasks:
                    task_new = input("Entar your task new:")
                    index_ = tasks.index(task)
                    tasks[index_] = task_new
                    save_tasks(task)
                    print("Updated!!")
                return f"Not found the task in tasks {task}"

            elif choes in "4":
                if tasks :
                    for i, task in enumerate(tasks):
                        print(f"{i+1}. {tasks[i]}")
                return f"Tasks is empty!!"
                
            elif  choes in "5":
                print("Good bye!!")
                break

            elif choes == " ":
                continue
            
            else:
                print("Invalid choice. Please try again.")
        
        except Exception as e:
            print("Error",e)

if __name__ == "__main__":
    main()
    