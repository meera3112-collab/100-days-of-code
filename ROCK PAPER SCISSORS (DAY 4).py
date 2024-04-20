

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

user_input=int(input("Enter 0 for rock, 1 for paper and 2 for scissor :"))
if user_input>2:
    print("Invalid Input!!! give an valid input")
else:
    
    if user_input==0:
        print(rock)
    elif user_input==1:
        print(paper)
    else:
        print(scissors)
    print("Computer's choice :");

import random;
computer_input=random.randint(0,2);
#print("Computer's choice :");
if user_input<=2:
    if computer_input==0:
        print(rock)
    elif computer_input==1:
        print(paper)
    else:
        print(scissors)

    if user_input==0 and computer_input==2:
        print("You won !!!")

    elif user_input==1 and computer_input==0:
        print("You won !!!")

    elif user_input==2 and computer_input==1:
        print("You won !!!")

    elif user_input==computer_input:
        print("Draw !!! Try again")
    else :
        print("You Lost!!! Try Again ")




    
















