import random

execute_count = 0
win_count = 0
lose_count = 0

def again():
     global play_again
     play_again = input("Do you want to play again? press(yes for y) or (no for n):")
     
     
while True:    
     user_choice = input("Enter your choice(stone/paper/scissor):")
     computer_choice = random.choice(['stone','paper','scissor'])
     print(f'user choice is {user_choice}\ncomputer choice is {computer_choice}')
    
     if user_choice in ['stone','paper','scissor']:
         if user_choice == computer_choice:
           print(f"Both players selected the {user_choice}.It's a tie.")
         
         elif user_choice == 'stone':
           if computer_choice == "paper":
              print("The paper cover the stone! you lose.")
              lose_count += 1
           elif computer_choice == "scissor" :
              print("The stone broke the scissor! you win!")
              win_count += 1
              
         elif user_choice == "paper":
           if computer_choice == "stone":
              print("The paper cover the stone! you win!")
              win_count += 1
           elif computer_choice =="scissor":
              print("The scissors cut the paper! you lose.")
              lose_count += 1
             
         elif user_choice == "scissor":
          if computer_choice == "stone":
              print("The stone broke the scissor! you lose")
              lose_count += 1
          elif computer_choice =="paper":
              print("The scissors cut the paper! you win.")
              win_count += 1
         execute_count += 1    
         again()
         if play_again in ['y','n','Y','N']:
           if play_again.lower() =='n':
              print(f"you played the game for {execute_count} times.\nyour score is {win_count}.\nyou lose for {lose_count} times.") 
              break
         else:
              print(f"Invalid input {play_again}.please enter the vaild input given below")
              again()
     else:
       print(f"Invalid choice {user_choice}.\nEnter the given below choices(stone/paper/scissor). ")
                     
