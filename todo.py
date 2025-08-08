# File name: todo.py
# Features: Persistent storage using file handling, list management, string operations

# File to store tasks
TASKS_FILE = "tasks.txt"

# --- Load tasks from file (File Handling + Lists + String Manipulation) ---
def load_tasks():
    tasks = []
    try:
        with open(TASKS_FILE, "r") as file:
            for line in file:
                tasks.append(line.strip())  # strip() removes \n (string manipulation)
    except FileNotFoundError:
        pass  # If file doesn't exist yet, return empty list
    return tasks

# --- Save tasks back to file (File Handling + Lists) ---
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")  # String concatenation to add newline

# --- Display all tasks (Lists) ---
def view_tasks(tasks):
    if not tasks:
        print("\n📂 No tasks in your To-Do list.")
    else:
        print("\n📝 Your To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

# --- Add a new task (Lists + String Manipulation) ---
def add_task(tasks):
    task = input("\nEnter new task: ").strip()  # strip() removes spaces
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("✅ Task added successfully.")
    else:
        print("⚠️ Task cannot be empty.")

# --- Remove a task (Lists) ---
def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("\nEnter task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)  # Remove by index
                save_tasks(tasks)
                print(f"🗑 Task '{removed_task}' removed.")
            else:
                print("⚠️ Invalid task number.")
        except ValueError:
            print("⚠️ Please enter a valid number.")

# --- Main Program Loop ---
def main():
    tasks = load_tasks()

    while True:
        print("\n--- 📋 TO-DO LIST MENU ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("👋 Exiting To-Do List. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
