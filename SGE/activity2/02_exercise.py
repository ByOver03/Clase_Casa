list1 = []
list2 = []
list3 = []

for i in range(5):
    while True:
        try:
            num = int(input(f"Introduce elemento {i+1} para list1: "))
            break
        except ValueError:
            print("Entrada no válida. Introduce un número entero.")
    list1.append(num)
    while True:
        try:
            num = int(input(f"Introduce elemento {i+1} para list2: "))
            break
        except ValueError:
            print("Entrada no válida. Introduce un número entero.")
    list2.append(num)

    
for a, b in zip(list1, list2):
    list3.append(a + b)

print("list1 =", list1)
print("list2 =", list2)
print("list3 =", list3)