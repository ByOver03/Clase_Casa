print("enter your grade")
grade = int(input())

if grade >= 9 and grade <= 10:
    print("Outstanding")
elif grade >=7 and grade <= 8:
    print("Good")
elif grade >=5 and grade <=6:
    print("Pass")
elif grade >=0 and grade <=4:
    print("Fail")
else:
    print("Invalid grade")