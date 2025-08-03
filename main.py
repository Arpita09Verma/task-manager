from taskmanager import load_tasks, add_task, view_task, update_task, delete_task, mark_task_as_complete

def main():
    load_tasks()
    while True:
        print("\nInteractive Task Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark a task as complete")
        print("6. Exit")

        choice = input("Select an option (1-6): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            mark_task_as_complete()
        elif choice == "6":
            print("Exiting the Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1-5).")

if __name__ == "__main__":
    main()
