#This is a program to pull the initials from a name typed in all lower case
#Je'Vaughn Black
#IPT100-02
#Excercise 03
#program.py

name = input("Enter your full name: ")
#The .split method allowed me to seperate each part of the name into a list
name_list = name.split()
#The number is the names position on the list, counting up from 0
first_name = name_list[0]
middle_name = name_list[1]
last_name = name_list[2]
#with the names in the format of a list, I was able to use indexing to pull the first letter.
print(f"{first_name.upper()[0]}.{middle_name.upper()[0]}.{last_name.upper()[0]}")
