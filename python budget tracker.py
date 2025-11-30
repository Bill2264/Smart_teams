import tkinter as tk
from tkinter import ttk, messagebox, simpledialog


#Class with budget tracker

class ExpenseTracker:
    def __init__(self, date, description, amount):
        self.date = date
        self.description = description
        self.amount= amount


def add_expense(self, expense):
    self.expenses.append(expense)

def remove_expense(self, index):
    if 0 <= index < len(self.expenses):
        del self.expenses[index]
        print("Expense removed successfully.")

    else:
            print ("Invalid index. No expense removed.")
def add_expense(expenses):
    date = input("Enter date (YYYY-MM-DD): ")
    description = input("Enter description: ")
    amount = float(input("Enter amount: "))
    expense = ExpenseTracker(date, description, amount)
    expenses.append(expense)
    
expenses = []  # must be BEFORE the loop

while True:
    # Initial attempt at making the very basic layout of the budget tracker
    print("Expense Tracker Menu:")
    print("1. Add Expense")
    print("2. Remove Expense")
    print("3. View Expense")
    print("4. Total Expense")
    print("5. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_expense(expenses)

    if choice == '2':
        remove_expense(expenses)

    if choice == '3':
        view_expenses(expenses)

    if choice == '4':
        total_expense(expenses)

    if choice == '5':
        edit_expense(expenses)

    if choice == '6':
        print("Exited Successfully")
        break

def view_expenses(expenses):
    if not expenses:
        print("No expenses to show.")
        return
    print("Expenses:")
    for idx, expense in enumerate(expenses):
        print(f"{idx}. Date: {expense.date}, Description: {expense.description}, Amount: {expense.amount}")