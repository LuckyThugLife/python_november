def add_task(tasks: list):
    task = input("Enter the task you want to add: ")
    tasks.append(task)
    print(f"Task '{task}' has been added to the list.")

def remove_task(tasks: list):
    if not tasks:
        print("The list is empty.")
        return
    index = input("Enter the index of the task you want to remove: ")
    try:
        index = int(index)
        if index < 0 or index >= len(tasks):
            raise ValueError
    except ValueError:
        print("Invalid index. Please enter a valid index.")
        return
    task = tasks.pop(index)
    print(f"Task '{task}' has been removed from the list.")

def view_list(tasks: list):
    if not tasks:
        print("The list is empty.")
        return
    print("Current list of tasks:")
    for i, task in enumerate(tasks):
        print(f"{i}. {task}")

def main():
    tasks = []
    while True:
        print("To-Do List Operations:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View List")
        print("4. Exit Program")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            remove_task(tasks)
        elif choice == "3":
            view_list(tasks)
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a valid choice.")

if __name__ == "__main__":
    main()