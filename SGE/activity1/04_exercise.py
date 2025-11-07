print("Enter the age")
age= int(input())
print("Enter the years of expirience")
years_of_expirience= int(input())
print("Does the person have a university degree? (yes/no)")
university_degree= input()

if university_degree == "yes" and age >= 21 and years_of_expirience >=2:
    print("The person is qualyfied")
else:
    print("The person is not qualyfied")