todo_list = []

def main_menu():
    print("\n--To-Do List Menu--")
    print("1. View your To-Do List!")
    print("2. Add a task!!!")
    print("3. Delete a task :((")
    print("4.Close the program")

def ToDo_List():
    if len(todo_list) == 0:
        print("Your To-Do List is empty.")
    else:
        print("\n--Your To-Do List--")
        for idx, task in enumerate(todo_list, 1):
            print(f"{idx}. {task}")

def Add_Task():
    task = input("Enter your task: ")
    todo_list.append(task)
    print(f"\n'{task}' has been added to your To-Do List")

def Delete_Task():
    try:
        ToDo_List()
        task_num = int(input("\nEnter the task number you want to remove: "))
        removed_task = todo_list.pop(task_num - 1)
        print(f"'{removed_task}' has been removed from your To-Do List")
    except(ValueError, IndexError):
        print("\nPlease enter a valid task number.")


while True:
    main_menu()

    choice = input("What do you want to do? (1-4): ")

    if choice == '1':
        ToDo_List()
    elif choice == '2':
        Add_Task()
    elif choice == '3':
        Delete_Task()
    elif choice == '4':
        print("\nSee you again! Exiting the To-Do List...")
        break
    else:
        print("\nInvalid choice! Choose a number between 1 and 4.")    
            