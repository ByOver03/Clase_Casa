grades =0
nonpassingGrade = []
passingGrade = []

while True:
    grade= int(input("Enter a grade between 0 and 10: "))
    if grade <=5 and grade >=0:
        nonpassingGrade.append(grade)
    elif grade >5 and grade <=10:
        passingGrade.append(grade)
    else:
        print("invalid grade")
        break

print("Non passing grades:", nonpassingGrade)
print("Passing grades:", passingGrade)
print("All grades:", nonpassingGrade + passingGrade)