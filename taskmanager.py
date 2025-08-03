from datetime import datetime
import json

tasks = []


def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)


def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
            # Add default priority if missing
            for task in tasks:
                if 'priority' not in task:
                    task['priority'] = 'Medium'  # or whatever default you prefer
    except FileNotFoundError:
        tasks = []

def add_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    while True:
        priority = input("Enter priority (High / Medium / Low): ").capitalize()
        if priority in ["High", "Medium", "Low"]:
            break
        print("Invalid priority. Please enter High, Medium, or Low.")

    while True:
        due_date = input("Enter due date (YYYY-MM-DD): ")
        try:
            datetime.strptime(due_date, "%Y-%m-%d")  # Validate date format
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    tasks.append({
        "title": title,
        "description": description,
        "status": "pending",
        "due_date": due_date,
        "priority": priority
    })
    print("Task added successfully")
    save_tasks()


def view_task():
    if tasks:
        print("\nTasks:")
        for idx, task in enumerate(tasks, start=1):
            # Safely get all fields with defaults
            title = task.get('title', 'No title')
            description = task.get('description', 'No description')
            status = task.get('status', 'pending')
            due_date = task.get('due_date', 'No due date')
            priority = task.get('priority', 'Medium')

            print(f"{idx}. Title: {title}, Description: {description}, "
                  f"Status: {status}, Due date: {due_date}, Priority: {priority}")
    else:
        print("No tasks available.")


def update_task():
    view_task()
    if tasks:
        try:
            task_index = int(input("Enter the index of the task to update: ")) - 1
            if 0 <= task_index < len(tasks):
                new_title = input("Enter new title (Press Enter to skip): ")
                if new_title:
                    tasks[task_index]['title'] = new_title

                new_description = input("Enter new description (Press Enter to skip): ")
                if new_description:
                    tasks[task_index]['description'] = new_description

                new_priority = input("Enter new priority (High/Medium/Low) (Press Enter to skip): ").capitalize()
                if new_priority and new_priority in ["High", "Medium", "Low"]:
                    tasks[task_index]['priority'] = new_priority

                new_due_date = input("Enter new due date (YYYY-MM-DD) (Press Enter to skip): ")
                if new_due_date:
                    try:
                        datetime.strptime(new_due_date, "%Y-%m-%d")
                        tasks[task_index]['due_date'] = new_due_date
                    except ValueError:
                        print("Invalid date format. Date not updated.")

                print("Task updated successfully!")
            else:
                print("Invalid task index.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("No tasks available.")
    save_tasks()


def delete_task():
    view_task()
    if tasks:
        try:
            task_index = int(input("Enter the index of the task to delete: ")) - 1
            if 0 <= task_index < len(tasks):
                deleted_task = tasks.pop(task_index)
                print(f"Task '{deleted_task['title']}' deleted successfully!")
            else:
                print("Invalid task index.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("No tasks available.")
    save_tasks()


def mark_task_as_complete():
    view_task()
    if tasks:
        try:
            task_index = int(input("Enter the index of the task to mark as complete: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["status"] = "complete"
                print(f"Task '{tasks[task_index]['title']}' marked as complete! 🎉")
            else:
                print("Invalid task index.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("No tasks available.")
    save_tasks()