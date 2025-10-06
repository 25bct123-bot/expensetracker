import csv
import os

FILE_NAME = 'expenses.csv'

# Define expense fields
fields = ['Date', 'Category', 'Amount', 'Description']

# Load existing expenses from CSV
def load_expenses():
    expenses = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append(row)
    return expenses

# Save expenses to CSV
def save_expenses(expenses):
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(expenses)

# Add a new expense
def add_expense(expenses):
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g., Food, Transport): ")
    amount = input("Enter amount: ")
    description = input("Enter description: ")

    expense = {
        'Date': date,
        'Category': category,
        'Amount': amount,
        'Description': description
    }
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully.\n")

# View all expenses
def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return
    print("\n--- All Expenses ---")
    for e in expenses:
        print(f"{e['Date']} | {e['Category']} | ${e['Amount']} | {e['Description']}")
    print()

# Filter expenses by category
def filter_by_category(expenses):
    category = input("Enter category to filter: ")
    filtered = [e for e in expenses if e['Category'].lower() == category.lower()]
    if not filtered:
        print("No expenses found for this category.")
    else:
        print(f"\n--- Expenses in '{category}' ---")
        for e in filtered:
            print(f"{e['Date']} | ${e['Amount']} | {e['Description']}")
    print()

# Main menu
def main():
    expenses = load_expenses()

    while True:
        print("=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter by Category")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            filter_by_category(expenses)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
