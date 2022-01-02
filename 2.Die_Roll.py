import random
count = 0
total_point = 0
while int(input("press 1 to roll the die or 0 to exist:")):
    n = random.randint(1,6)
    total_point += n 
    print("you got",n)
    count += 1
print(f"you roll the die for {count} times.\nyour total score {total_point}")
 
