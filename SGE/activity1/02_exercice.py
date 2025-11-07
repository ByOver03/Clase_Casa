#Ask for the numbers
print("Insert the first number to calculate:")
num1=int(input())
print("Insert the second number to calculate:")
num2=int(input())

#Show the results of the operations
print(num1, "+", num2, num1 + num2)
print(num1, "-", num2, num1 - num2)
print(num1, "*", num2, num1 * num2)
res = num1 / num2
print(num1, "/", num2, res.__round__(1))
print(num1, "^", num2, (num1 ** num2))

