numbers = []
option = 0
a = __import__('time')
while option != 9:
    print("1. Add a number at the end")
    print("2. Insert a number at a specific position")
    print("3. Show the length of the list")
    print("4. Remove the last number")
    print("5. Remove a number by position")
    print("6. Count how many times a number appears")
    print("7. Show all positions of a number")
    print("8. Display all numbers")
    print("9. Exit")
    option = int(input("Select an option: "))
    # 1.Add a number at the end
    if option == 1:
        numbers.append(int(input("Enter the number to add: ")))
        a.sleep(1)
    # 2.Insert a number at a specific position
    elif option == 2:
        pos = int(input("Enter the position to insert the number: "))
        num = int(input("Enter the number to insert: "))
        numbers.insert(pos, num)
        a.sleep(1)
    # 3.Show the length of the list.
    elif option == 3:
        print(f"Length of the list: {len(numbers)}")
        a.sleep(1)
    # 4.Remove the last number
    elif option == 4:
        if numbers:
            numbers.pop()
        else:
            print("The list is empty.")
        a.sleep(1)
    # 5.Remove a number by position.
    elif option == 5:
        print("=======================================================================")
        for i, num in enumerate(numbers):
            print(f"{i}. {num}")
        print("=======================================================================")
        pos = int(input("Enter the position of the number to remove: "))
        if 0 <= pos < len(numbers):
            numbers.pop(pos)
        else:
            print("Invalid position.")
        a.sleep(1)
    # 6.Count how many times a number appears.
    elif option == 6:
        num = int(input("Enter the number to count: "))
        count = numbers.count(num)
        print(f"The number {num} appears {count} times.")
        a.sleep(1)
    # 7.Show all positions of a number.
    elif option == 7:
        num = int(input("Enter the number to find positions: "))
        positions = [i for i, x in enumerate(numbers) if x == num]
        print(f"The number {num} is found at positions: {positions}")
        a.sleep(1)
    # 8.Display all numbers.
    elif option == 8:
        print("=======================================================================")
        for i, num in enumerate(numbers):
            print(f"{i}. {num}")
        print("=======================================================================")
        a.sleep(1)
    # 9.Exit#
    elif option == 9:
        break
    else:
        print("Invalid option, please try again.")
        a.sleep(1)