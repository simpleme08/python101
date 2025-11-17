import csv
import os

DATA_FILE = "tasks.csv"

# Load tasks from CSV
def load_tasks():
    tasks = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                tasks.append(row)
    return tasks

# Save tasks to CSV
def save_tasks(tasks):
    with open(DATA_FILE, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['task', 'status']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for t in tasks:
            writer.writerow(t)
    print("Tasks saved!")

# Add a new task
def add_task(tasks):
    task_name = input("Enter task name: ").strip()
    if task_name:
        tasks.append({"task": task_name, "status": "Pending"})
        print(f"Task '{task_name}' added.")
    else:
        print("Task cannot be empty.")

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print("\n--- Tasks ---")
    for i, t in enumerate(tasks, start=1):
        print(f"{i}. {t['task']} [{t['status']}]")
    print("------------")

# Mark task as done
def mark_done(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num-1]['status'] = "Done"
            print(f"Task '{tasks[num-1]['task']}' marked as done.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Enter a valid number.")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num-1)
            print(f"Task '{removed['task']}' deleted.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Enter a valid number.")

# Main menu
def main():
    tasks = load_tasks()

    while True:
        print("\nAuto-Task Bot")
        print("1) Add Task")
        print("2) View Tasks")
        print("3) Mark Task as Done")
        print("4) Delete Task")
        print("5) Save & Quit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_done(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Pick 1-5.")

if __name__ == "__main__":
    main()
