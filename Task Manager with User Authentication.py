
import hashlib

# Function for user registration
def register():
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    # Hash the password for security
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Store the credentials in a file
    with open('users.txt', 'a') as file:
        file.write(f"{username},{hashed_password}\n")
    print("Registration successful!")


# Function for user login
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Hash the entered password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Verify credentials
    with open('users.txt', 'r') as file:
        for line in file:
            stored_username, stored_password = line.strip().split(',')
            if stored_username == username and stored_password == hashed_password:
                print("Login successful!")
                return True, username
    print("Invalid credentials, please try again.")
    return False, None








# Function to add a new task
def add_task(username):
    task = input("Enter the task description: ")
    with open(f'tasks_{username}.txt', 'a') as file:
        task_id = sum(1 for line in open(f'tasks_{username}.txt')) + 1
        file.write(f"{task_id},{task},Pending\n")
    print("Task added successfully.")



# Function to view tasks
def view_tasks(username):
    print("\nYour Tasks:")
    with open(f'tasks_{username}.txt', 'r') as file:
        for line in file:
            task_id, task, status = line.strip().split(',')
            print(f"Task ID: {task_id}, Task: {task}, Status: {status}")



# Function to mark a task as completed
def mark_task_completed(username):
    task_id = input("Enter the task ID to mark as completed: ")
    tasks = []
    with open(f'tasks_{username}.txt', 'r') as file:
        for line in file:
            task_id_in_file, task, status = line.strip().split(',')
            if task_id_in_file == task_id:
                status = "Completed"
            tasks.append(f"{task_id_in_file},{task},{status}")
    with open(f'tasks_{username}.txt', 'w') as file:
        for task in tasks:
            file.write(task + '\n')
    print("Task marked as completed.")



# Function to delete a task
def delete_task(username):
    task_id = input("Enter the task ID to delete: ")
    tasks = []
    with open(f'tasks_{username}.txt', 'r') as file:
        for line in file:
            task_id_in_file, task, status = line.strip().split(',')
            if task_id_in_file != task_id:
                tasks.append(f"{task_id_in_file},{task},{status}")
    with open(f'tasks_{username}.txt', 'w') as file:
        for task in tasks:
            file.write(task + '\n')
    print("Task deleted successfully.")
    
    

# Main menu after user logs in
def task_manager_menu(username):
    while True:
        print("\n1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Logout")
        choice = input("Enter your choice: ")
        if choice == '1':
            view_tasks(username)
        elif choice == '2':
            add_task(username)
        elif choice == '3':
            mark_task_completed(username)
        elif choice == '4':
            delete_task(username)
        elif choice == '5':
            print("Logging out...")
            break
        else:
            print("Invalid choice, please try again.")
            

# Main program flow for registration and login
def main():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            register()
        elif choice == '2':
            logged_in, username = login()
            if logged_in:
                task_manager_menu(username)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

# Start the program
main()
