name = ""
age = 0
city = ""

#ask for name, age and city
print("What's your name?")
name = input()
print("How old are you?")
age = int(input())
print("Which city do you live in?")
city = input()

#We put the name in title so the first letter is in capital letter
name = name.strip().title()

#Show the data in three different ways
print(f"Name: {name} Age: {age} City: {city}")
print("Name: "+name + " Age: " + str(age) + " City: "+ city)
print("Name: ", name, " Age: ", age, " City: ", city)