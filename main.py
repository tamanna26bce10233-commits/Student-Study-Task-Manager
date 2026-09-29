from modules.task import Task
from modules.storage import add_task, get_tasks, search_task, complete_task
from modules.validation import validate_task_title
from modules.reports import show_progress
from modules.menu import display_menu


while True:
    display_menu()

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        title = input("Enter your study task: ")

        valid, result = validate_task_title(title)

        if valid:
            task = Task(result)
            add_task(task)
            print("Task added successfully!")
        else:
            print(result)

    elif choice == "2":
        print("\nYour study tasks:")

        tasks = get_tasks()

        if not tasks:
            print("No tasks added yet.")
        else:
            for task in tasks:
                if task.completed:
                    print("-", task.title, "[Completed]")
                else:
                    print("-", task.title, "[Pending]")

    elif choice == "3":
        keyword = input("Enter a keyword to search: ")

        print("Search results:")

        results = search_task(keyword)

        if results:
            for task in results:
                print("-", task.title)
        else:
            print("No matching task found.")

    elif choice == "4":
        title_to_complete = input("Enter the task you completed: ")

        if complete_task(title_to_complete):
            print("Task marked as completed!")
        else:
            print("Task not found.")

    elif choice == "5":
        print("\nStudy Progress:")
        show_progress(get_tasks())

    elif choice == "6":
        print("Thank you for using Student Study Task Manager!")
        break

    else:
        print("Invalid choice. Please try again.")
        