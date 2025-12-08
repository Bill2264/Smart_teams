from Calculations import Calculations

calc = Calculations()

def add_expense_terminal():
    date = input("Enter date (DD-MM-YYYY): ")
    amount = input("Enter amount: ")
    category = input("Enter category (e.g., Food, Rent, Transport): ")
    
    warning = calc.add_expense(date, amount, category)
    print("\n\nExpense added successfully!")
    if warning:
        print(f" {warning}")

def remove_expense_terminal():
    if not calc.get_all():
        print("\n\nNo expense to remove. ")
        return
    
    view_expenses_terminal()
    try:
        index = int(input("Enter the index of the expense to remove: "))
        if 0 <= index < len(calc.get_all()):
            calc.remove_expense(index)
            print("\n\nExpense removed successfully!")
        else:
            print("\n\nInvalid index. No expense removed.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def edit_expense_terminal():
    view_expenses_terminal()
    index = int(input("Enter the index of the expense to edit: "))
    date = input("Enter new date (DD-MM-YYYY): ")
    amount = input("Enter new amount: ")
    category = input("Enter new category: ")
    warning = calc.edit_expense(index, date, amount, category)
    print("\n\nExpense edited successfully!")
    if warning:
        print(f" {warning}")

def view_expenses_terminal():
    expenses = calc.get_all()
    if not expenses:
        print("\n\nNo expenses to show.")
        return
    else:
        print("\nIndex | Date       | Amount   | Category")
    print("-"*50)
    for idx, exp in enumerate(expenses):
        print(f"{idx:<5} | {exp[0]:<10} | {exp[1]:<8} | {exp[2]:<10}")

def total_expense_terminal():
    total = calc.get_total()
    print(f"\n\nTotal expenses: {total}")

def weekly_budget_terminal():
    amount = input("Enter your weekly budget amount: ")
    calc.set_weekly_budget(amount)
    print("\n\nWeekly budget set successfully!")

def weekly_total_terminal():
    total = calc.get_weekly_total()
    print(f"\n\nTotal spent this week: {total}")
    warning = calc.budget_warning()
    if warning:
        print(f" {warning}")

while True:
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. Remove Expense")
    print("3. Edit Expense")
    print("4. View Expenses")
    print("5. Total Expenses")
    print("6. Set Weekly Budget")
    print("7. Weekly Total & Warning")
    print("8. Exit")
    
    choice = input("Enter your choice (1-8): ")
    
    if choice == '1':
        add_expense_terminal()
    elif choice == '2':
        remove_expense_terminal()
    elif choice == '3':
        edit_expense_terminal()
    elif choice == '4':
        view_expenses_terminal()
    elif choice == '5':
        total_expense_terminal()
    elif choice == '6':
        weekly_budget_terminal()
    elif choice == '7':
        weekly_total_terminal()
    elif choice == '8':
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")
