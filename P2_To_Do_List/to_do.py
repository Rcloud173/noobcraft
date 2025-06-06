# # Simple To-Do List Program

# todo_list = []

# def show_menu():
#     print("\n--- To-Do List ---")
#     print("1. Show To-Do List")
#     print("2. Add Task")
#     print("3. Remove Task")
#     print("4. Exit")

# def show_tasks():
#     if not todo_list:
#         print("Your to-do list is empty.")
#     else:
#         print("\nYour Tasks:")
#         for i, task in enumerate(todo_list, 1):
#             print(f"{i}. {task}")

# def add_task():
#     task = input("Enter a task: ")
#     todo_list.append(task)
#     print(f"Task '{task}' added.")

# def remove_task():
#     show_tasks()
#     try:
#         task_num = int(input("Enter task number to remove: "))
#         if 1 <= task_num <= len(todo_list):
#             removed = todo_list.pop(task_num - 1)
#             print(f"Task '{removed}' removed.")
#         else:
#             print("Invalid task number.")
#     except ValueError:
#         print("Please enter a valid number.")

# while True:
#     show_menu()
#     choice = input("Choose an option (1-4): ")
    
#     if choice == "1":
#         show_tasks()
#     elif choice == "2":
#         add_task()
#     elif choice == "3":
#         remove_task()
#     elif choice == "4":
#         print("Goodbye!")
#         break
#     else:
#         print("Invalid choice. Please enter a number from 1 to 4.")
 
# this is written by ai write it on your own if and only if use it for Reference

print("this is a to-do list")

def show_menu():
    print("\n--- To-Do List ---")
    print("1. Show To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

show_menu()