print("Enter the first salary: ")
salary1=int(input())
print("Enter the second salary: ")
salary2=int(input())
res=0

if salary1>salary2:
    res = salary1 - salary2
    print("Salary1 is greater than Salary2 by", res, "€ ")
elif salary1<salary2:
    res = salary2 - salary1
    print("Salary2 is greater than Salary1 by", res, "€ ")
else:
    print("Both salaries are equal")