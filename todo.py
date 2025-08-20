# Simple To-Do List in Python

tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added!")

def view_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def delete_task(index):
    if 0 < index <= len(tasks):
        removed = tasks.pop(index - 1)
        print(f"Task '{removed}' removed!")
    else:
        print("Invalid task number.")

# Example usage
add_task("Finish internship form")
add_task("Upload project to GitHub")
view_tasks()
delete_task(1)
view_tasks()
