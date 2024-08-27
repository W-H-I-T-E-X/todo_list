# To-Do List Application

# List to store tasks
tasks = []

# Function to add a new task
def add_task():
    task = input("Enter task title: ")
    description = input("Enter task description (optional): ")
    tasks.append({"id": len(tasks) + 1, "task": task, "description": description, "status": "Incomplete"})
    print("Task added successfully!")

# Function to view all tasks
def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        for task in tasks:
            status = "✓" if task["status"] == "Complete" else "✗"
            print(f"ID: {task['id']} | Task: {task['task']} | Status: {status} | Description: {task['description']}")

# Function to update a task
def update_task():
    task_id = int(input("Enter task ID to update: "))
    for task in tasks:
        if task["id"] == task_id:
            new_task = input(f"New Task Title (current: {task['task']}): ") or task['task']
            new_description = input(f"New Description (current: {task['description']}): ") or task['description']
            task.update({"task": new_task, "description": new_description})
            print("Task updated successfully!")
            return
    print("Task not found.")

# Function to mark a task as complete
def complete_task():
    task_id = int(input("Enter task ID to mark as complete: "))
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "Complete"
            print("Task marked as complete!")
            return
    print("Task not found.")

# Function to delete a task
def delete_task():
    task_id = int(input("Enter task ID to delete: "))
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            print("Task deleted successfully!")
            return
    print("Task not found.")

# Function to display the main menu
def main_menu():
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark Task as Complete")
        print("5. Delete Task")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            complete_task()
        elif choice == "5":
            delete_task()
        elif choice == "6":
            print("Exiting the To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Start the application
if __name__ == "__main__":
    main_menu()
