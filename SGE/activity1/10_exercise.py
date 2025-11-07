MAX_ATTEMPTS = 3
CORRECT_PASSWORD = "secret"

for attempt in range(1, MAX_ATTEMPTS + 1):
    pwd = input("Enter password: ")
    if pwd == CORRECT_PASSWORD:
        print("Acces granted")
        break
    else:
        print(f"Wrong password ({attempt}/{MAX_ATTEMPTS})")
else:
    print("Account locked")
