tasks = []
option = 0
a = __import__('time')
while option != 6:
    print("1. Add new task")
    print("2. Display total number of tasks")
    print("3. Remove a task by position")
    print("4. Delete all tasks")
    print("5. Show all pending tasks")
    print("6. Exit")
    option = int(input("Select an option: "))
    # 1 add new tasks to the list
    if option ==1:
        tasks.append(input("Enter the new task: "))
        a.sleep(1)
    # 2 Display the total number of tasks
    elif option ==2:
        print(f"Total number of tasks: {len(tasks)}")
        a.sleep(1)
    # 3 remove a task by position
    elif option ==3:
        print("=======================================================================")
        for i in range(len(tasks)):
            print(f"{i+1}. {tasks[i]}")
        print("=======================================================================")
        tasks.pop(int(input("Enter the position of the task to remove: "))-1)
        a.sleep(1)
    # 4 delete all tasks
    elif option ==4:
        tasks.clear()
        a.sleep(1)
    # 5 show all pending tasks
    elif option ==5:
        print("=======================================================================")
        for i in range(len(tasks)):
            print(f"{i+1}. {tasks[i]}")
        print("=======================================================================")
        a.sleep(1)
    # 6 exit
    elif option ==6:
        break
    else:
        print("Invalid option, please try again.")
        a.sleep(1)