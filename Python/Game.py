import random
dict = {"1":"Snake","2":"Water","3":"Gun"}
snake = list (dict.keys())[0]
water = list (dict.keys())[1]
gun = list (dict.keys())[2]
turns = int(input("How many games do you want to play?: "))
gamesCount = 0
comp = []
user = []
choice = ""
while turns>0:
    gamesCount += 1
    compTurn = random.choice(list(dict.keys()))
    while choice not in list (dict.keys()):
        print(f"Games No. {gamesCount}")
        print("------------")
        for key, value in dict.items():
            print(f"Select {key} for {value}: ")
        choice = input()
        userTurn = choice
        if(choice not in list(dict.keys())):
            print("Incorrect option selected. Try again...!!!")
    choice=""
    if compTurn == snake:
        if userTurn == water:
            print(f"Computer won. Computer selected {dict[compTurn]} and you selected {dict[userTurn]}")
            comp.append(f"Won [{dict[compTurn]}]")
            user.append(f"Lost [{dict[userTurn]}]")
        elif userTurn == gun:
            print(f"You won. Computer selected {dict[compTurn]} and you selected {dict[userTurn]}")
            comp.append(f"Lost [{dict[compTurn]}]")
            user.append(f"Won [{dict[userTurn]}]")
        elif userTurn == snake:
            print(f"Match Tied. Computer selected {dict[compTurn]} and you also selected {dict[userTurn]}")
            comp.append(f"Tied [{dict[compTurn]}]")
            user.append(f"Tied [{dict[userTurn]}]")
    elif compTurn == water:
        if userTurn == gun:
            print(f"Computer won. Computer selected {dict[compTurn]} and you selected {dict[userTurn]}")
            comp.append(f"Won [{dict[compTurn]}]")
            user.append(f"Lost [{dict[userTurn]}]")
        elif userTurn == snake:
            print(f"You won. Computer selected {dict[compTurn]} and you selected {dict[userTurn]}")
            comp.append(f"Lost [{dict[compTurn]}]")
            user.append(f"Won [{dict[userTurn]}]")
        elif userTurn == water:
            print(f"Match Tied. Computer selected {dict[compTurn]} and you also selected {dict[userTurn]}")
            comp.append(f"Tied [{dict[compTurn]}]")
            user.append(f"Tied [{dict[userTurn]}]")
    elif compTurn == gun:
        if userTurn == snake:
            print(f"Computer won. Computer selected {dict[compTurn]} and you selected {dict[userTurn]}")
            comp.append(f"Won [{dict[compTurn]}]")
            user.append(f"Lost [{dict[userTurn]}]")
        elif userTurn == water:
            print(f"You won. Computer selected {dict[compTurn]} and you selected {dict[userTurn]}")
            comp.append(f"Lost [{dict[compTurn]}]")
            user.append(f"Won [{dict[userTurn]}]")
        elif userTurn == gun:
            print(f"Match Tied. Computer selected {dict[compTurn]} and you also selected {dict[userTurn]}")
            comp.append(f"Tied [{dict[compTurn]}]")
            user.append(f"Tied [{dict[userTurn]}]")
    turns -= 1
    if(turns == 0):
        compWinCount = sum("Won" in s for s in comp)
        userWinCount = sum("Won" in s for s in user)
        print("\n################################################################################")
        print("Game No    Computer Result       Your Result")
        print("---------------------------------------------")
        for index in range(len(comp)):
            # print(item1, end = ", ")
            print(f"    {index + 1}      {comp[index]}       {user[index]}")
        if compWinCount > userWinCount:
            print(f'''
Final Result
******************************************************************************
Bad Luck! Computer is the Winner. Computor won {compWinCount} game(s) and you won {userWinCount} game(s)...!!!
Better Luck next time...!!!
********************************************************************************''')
        elif compWinCount < userWinCount:
            print(f'''
Final Result
*************************************************************************
Congratulations!You are the Winner. Computor won {compWinCount} game(s) and you won {userWinCount} game(s)...!!!
***************************************************************************''')
        else:
            print(f'''
Final Result
*********************************************
Match tied. Both won {compWinCount} game(s)...!!!
***********************************************''')
        while True:
            playAgain = input("\nDo you want to play again? (Y/N): ")
            if playAgain.upper() == "Y":
                turns = int(input("\nHow many games do you want to play?: "))
                gamesCount = 0
                comp = []
                user = []
                break
            elif playAgain.upper() == "N":
                print("Thanks for playing...!!!")
                break
            else:
                print("Value should be either Y or N. Try again...!!!")
                continue
    continue