from random import *

print("Gmail ID generator")
first_name = input("Enter your first name:").capitalize()
last_name = input("Enter your last name:").capitalize()
full_name = first_name + last_name
num = "123457890"
gmail = full_name + "".join(sample(num, 3)) + "@gmail.com"
print("your Gmail ID is:", gmail)
