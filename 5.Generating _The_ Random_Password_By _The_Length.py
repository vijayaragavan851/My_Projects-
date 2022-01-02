print("random password generator.") # on 23.12.2021
import random
pass_len = int(input("Enter the length of the password:"))
char = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFHIJKLMNOPQRSTUVWXZ!@#$%^*()"
print(''.join(random.sample(char,pass_len)))
