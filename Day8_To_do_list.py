# Program for a to do list entry

task={}
def display_menu():
    print("\n====To-do list menu====")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as completed")
    print("4. Remove a task")
    print("=========================")

# function for adding a task
def add_task():
    task_name=input("Enter the task: ")

    if task_name in task:
        print(f"Task'{task_name}' already exists.")
    else:
        task[task_name]=False

# Function to view tasks
def view_task():
    if not task():
        print("No tasks available.")
    else:
        print("\n====To_do list====")
        for i,(task, completed) in enumerate(task.items(task.items(),1)):
            status = "✓" if completed else "✗"
            print(f"{i}.{task} [{status}]")

#Function to mark a task as completed

def mark_completed():
    task_name=input("Enter the task to mark as completed: ")
    if task_name in task:
        task[task_name]=True
        print(f"Task'{task_name}' marked as completd")
    else:
        print(f"Task'{task_name}' not found.")

#function to remove a task

def remove_task():
    task_name=input("Enter the task to remove: ")
    if task_name in task:
        del task[task_name]
        print(f"Task'{task_name}' removed.")
    else:
        print(f"Task'{task_name}' not found.")

#main loop

while True:
    display_menu()
    choice=input("Choose an option (1-5): ")

    if choice=="1":
        add_task()
    elif choice=="2":
        view_task()
    elif choice=="3":
        mark_completed()
    elif choice=="4":
        remove_task()
    elif choice=="5":
        print("Your tasks are saved!")
        break
else:
    print("Invalid choice. Please enter again!")


