import random

pass_len = int(input("Enter the length of the password:"))
char = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFHIJKLMNOPQRSTUVWXZ!@#$%^*()"
print(''.join(random.sample(char,pass_len)))
