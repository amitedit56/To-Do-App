#Simple to do App 

tasks = []

while True:
    print("\n--- TO DO APP ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    match choice:
        case "1":
            task  = input("Enter task : ")
            tasks.append(task)
            print("Task added successfully!")

        case "2":
            if not tasks:
                print("No tasks available!")
            else:
                print("\nYour Tasks")
                for i, task in enumerate (tasks, start=1):
                    print(f"{i}. {task}")
            
        case "3":
            if not tasks:
                print("No tasks to delete")
            else:
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")

                try:
                    num = int(input("Enter task number to delete : "))
                    if 1 <= num <= len(tasks):
                        removed = tasks.pop(num-1)
                        print(f"Task '{removed}' deleted!")
                    else:
                        print("Invalid task number!")
                        
                except Exception as err:
                    print(f"{err}")

        case "4":
            print("Exiting To Do App. Bye!")
            break

        case _:
            print("Invalid choice! Try again.")