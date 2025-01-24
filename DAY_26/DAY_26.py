from datetime import datetime

class Task:
    def __init__(self, title, due_date, priority):
        self.title = title
        self.due_date = due_date
        self.priority = priority

    def __str__(self):
        return f"[{self.priority}] {self.title} (Due: {self.due_date})"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, due_date, priority):
        task = Task(title, due_date, priority)
        self.tasks.append(task)
        print(f'Task "{title}" added successfully!')

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        print("\nTasks:")
        for index, task in enumerate(self.tasks):
            print(f"{index + 1}. {task}")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print(f'Task "{removed_task.title}" deleted successfully!')
        else:
            print("Invalid task index.")

    def edit_task(self, task_index, new_title, new_due_date, new_priority):
        if 0 <= task_index < len(self.tasks):
            task = self.tasks[task_index]
            task.title = new_title
            task.due_date = new_due_date
            task.priority = new_priority
            print(f'Task "{new_title}" updated successfully!')
        else:
            print("Invalid task index.")


def main():
    manager = TaskManager()

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Edit Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter the task title: ")
            due_date = input("Enter the due date (YYYY-MM-DD): ")
            priority = input("Enter the priority (High, Medium, Low): ")
            manager.add_task(title, due_date, priority)
        elif choice == '2':
            manager.view_tasks()
        elif choice == '3':
            manager.view_tasks()
            task_index = int(input("Enter the task number to delete: ")) - 1
            manager.delete_task(task_index)
        elif choice == '4':
            manager.view_tasks()
            task_index = int(input("Enter the task number to edit: ")) - 1
            new_title = input("Enter the new task title: ")
            new_due_date = input("Enter the new due date (YYYY-MM-DD): ")
            new_priority = input("Enter the new priority (High, Medium, Low): ")
            manager.edit_task(task_index, new_title, new_due_date, new_priority)
        elif choice == '5':
            print("Exiting the Task Manager.")
            break
        elif choice == " ":
            continue
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()