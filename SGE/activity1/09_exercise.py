print("Display a Word")
word = input()

for ch in word:
    if ch.lower() in "aeiou":
        continue
    print(ch.upper())