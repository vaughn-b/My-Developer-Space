# This is a program to determine age brackets
# Je'Vaughn Black
# IPT100-03WA
# Exercise 06a
# ageclass.py

print("Age Classifcation Program")
print("-" * 45)

age = float(input("Enter age: "))

while age > 0:
    if age <= 1:
        print("This person is an Infant")
    if 1 < age < 13:
        print("This person is a Child")
    if 13 <= age < 20:
        print("This person is a Teenager")
    if 20 <= age:
        print("This person is an Adult")
    age = float(input("Enter age: "))

print("Program has terminated properly")
