word = []
for i in range(5):
    word.append(input(f"Introduce elemento {i+1}: "))
    print(word)
word2 = word[::-1]
print(word2)