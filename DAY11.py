#ثبت هزینه ها 
class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def add_expense(self, description, amount):
        expense = {'description': description, 'amount': amount}
        self.expenses.append(expense)
        print(f"Expense added: {description} - ${amount:.2f}")

    def show_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return
        
        print("\nExpenses:")
        for expense in self.expenses:
            print(f"{expense['description']}: ${expense['amount']:.2f}")
        
        total = sum(expense['amount'] for expense in self.expenses)
        print(f"\nTotal Expenses: ${total:.2f}")

def main():
    manager = ExpenseManager()

    while True:
        print("\nExpense Manager")
        print("1. Add Expense")
        print("2. Show Expenses")
        print("3. Exit")
        
        choice = input("Choose an option (1/2/3): ")

        if choice == '1':
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: "))
            manager.add_expense(description, amount)
        elif choice == '2':
            manager.show_expenses()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()

