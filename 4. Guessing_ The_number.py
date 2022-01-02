import random

count = 0
win = 0
lose =0

while int(input("Do you want to play the number guessing game? press(yes for 1 / no for 0):")):
    number = random.randint(1,3)
    for i in range(1,4):
        user = int(input("guess the number:"))
        
        if False == bool(user):
            print('INVALID INIPUT.\nEnter your guess number from (1 to 10).')
            break
            
        elif user == number:
            print(f"you guessed the correct number in {i} try\nThe number is {user}.")
            win += 1
            break
        
    else :
        print(f"you guessed the wrong number.The number is {number}")
        lose += 1
        
    count += 1
print(f'you played the game for {count} times.\nyou win the game for {win} times.\nyou lose for {lose} times.')    
