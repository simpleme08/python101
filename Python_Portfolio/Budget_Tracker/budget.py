# budget.py - menu + validation + CSV save/load
import csv
import os

DATA_FILE = "data.csv"

def clear_screen():
    # Works on Windows/macOS/Linux in most terminals
    os.system('cls' if os.name == 'nt' else 'clear')

def load_expenses():
    expenses = []
    if not os.path.exists(DATA_FILE):
        return expenses
    with open(DATA_FILE, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert amount to float
            try:
                row['amount'] = float(row['amount'])
            except ValueError:
                row['amount'] = 0.0
            expenses.append(row)
    return expenses

def save_expenses(expenses):
    with open(DATA_FILE, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['item', 'amount', 'category']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for e in expenses:
            writer.writerow({
                'item': e.get('item',''),
                'amount': f"{e.get('amount',0):.2f}",
                'category': e.get('category','')
            })
    print("Saved to", DATA_FILE)

def add_expense(expenses):
    item = input("Item name: ").strip()
    if not item:
        print("Item name cannot be empty.")
        return
    while True:
        amt = input("Amount (numbers only): ").strip()
        try:
            amount = float(amt)
            break
        except ValueError:
            print("Invalid amount. Try again.")
    category = input("Category (e.g. food, rent, fun) [optional]: ").strip()
    expenses.append({'item': item, 'amount': amount, 'category': category})
    print("Expense added.")

def view_expenses(expenses):
    if not expenses:
        print("No expenses yet.")
        return
    print("\n--- Expenses ---")
    for i, e in enumerate(expenses, start=1):
        cat = f" [{e['category']}]" if e.get('category') else ""
        print(f"{i}. {e['item']}{cat} - ${e['amount']:.2f}")
    print("----------------")

def summary(expenses):
    if not expenses:
        print("No expenses to summarize.")
        return
    total = sum(e['amount'] for e in expenses)
    by_category = {}
    for e in expenses:
        cat = e.get('category') or 'Uncategorized'
        by_category[cat] = by_category.get(cat, 0) + e['amount']
    print(f"\nTotal spent: ${total:.2f}")
    print("By category:")
    for cat, amt in by_category.items():
        print(f"  {cat}: ${amt:.2f}")

def main():
    expenses = load_expenses()
    while True:
        print("\nBudget Tracker")
        print("1) Add expense")
        print("2) View expenses")
        print("3) Summary")
        print("4) Save")
        print("5) Load from file (overwrite current)")
        print("6) Clear all expenses")
        print("7) Quit")
        choice = input("Choose an option (1-7): ").strip()

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            summary(expenses)
        elif choice == '4':
            save_expenses(expenses)
        elif choice == '5':
            expenses = load_expenses()
            print("Loaded from file.")
        elif choice == '6':
            confirm = input("Are you sure? Type YES to clear: ").strip()
            if confirm == 'YES':
                expenses.clear()
                print("All expenses cleared.")
            else:
                print("Clear cancelled.")
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Pick a number 1-7.")

if __name__ == "__main__":
    main()
