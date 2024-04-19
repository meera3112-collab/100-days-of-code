print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
road=input("Your at an diversion.do you want to take right or left?");
if road=='Right' or road=='right':
    house=input("You are infront of an red and pink house. which house do you want to enter red or pink?")
    if house=='Red' or house=='red':
        print("The house is on fire. you are dead !!! GAME OVER")
    else:
        door=input("You have 2 doors infront of you. what do you wanna choose door1 or door2 (please enter door1 not just 1 or door2 not just 2)?")
        if door=="door1" or door=="Door1":
            print("It is an trap.you lost. GAME OVER !!!")
        else:
            print("Congrats you found the treasure. YOU WON ");
else:
    lake=input("You are infront of an lake. do you want to take a boat or swim?");
    if lake=='boat' or lake=='Boat':
        print("your boat is broken. you sunk.GAME OVER!!!")
    else:
        print("The lake is full of crocodile. you are eaten by one. GAME OVER !!!");
              
    
