import csv
import os

DATA_FILE = "passwords.csv"

def load_passwords():
    passwords = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                passwords.append(row)
    return passwords

def save_passwords(passwords):
    with open(DATA_FILE, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['account', 'username', 'password']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for p in passwords:
            writer.writerow(p)

def add_password(passwords):
    account = input("Account name (e.g., Gmail, Facebook): ").strip()
    username = input("Username or email: ").strip()
    password = input("Password: ").strip()
    passwords.append({"account": account, "username": username, "password": password})
    print("Password saved.")

def view_passwords(passwords):
    if not passwords:
        print("No passwords saved.")
        return
    print("\n--- Saved Passwords ---")
    for p in passwords:
        print(f"{p['account']} | {p['username']} | {p['password']}")
    print("----------------------")

def main():
    passwords = load_passwords()

    while True:
        print("\nPassword Manager")
        print("1) Add password")
        print("2) View passwords")
        print("3) Save and Quit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == '1':
            add_password(passwords)
        elif choice == '2':
            view_passwords(passwords)
        elif choice == '3':
            save_passwords(passwords)
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
