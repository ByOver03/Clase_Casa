import random

even =0
odd= 0
numbers = []
for i in range(10):
    numbers.append(random.randint(1, 100))
    if numbers[i] % 2 == 0:
        even +=1
    else:
        odd +=1
print("Generated numbers:", numbers)
print("Numbers sorted in ascending order", sorted(numbers))
print("Numbers sorted in descending order", sorted(numbers, reverse=True))

print("Largest number:", max(numbers), "Smallest number:", min(numbers))
print("Count of even numbers:", even, "Count of odd numbers:", odd)