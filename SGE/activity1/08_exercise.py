print("Display a number tu do a countdown")
number = int(input())
a = __import__('time')
while number != 0:
    print(number)
    number -= 1
    a.sleep(1)

print("Liftoff!")