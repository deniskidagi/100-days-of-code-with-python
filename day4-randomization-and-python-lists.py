import random

random_integer = random.randint(0,5)
print(random_integer)

#exercise: virtual coin toss game
coin_tossed = input("Choose head or tail")

computer_generated_coin = random.randint(1,2)
coin_phase = ""
if(computer_generated_coin == 1):
    coin_phase = "head"
else:
    coin_phase = "tail"

if coin_tossed == coin_phase:
    print(f"coin is {coin_phase}")
    print("You won")
else:
    print(f"coin is {coin_phase}")
    print("You lose try again")

#challenge: whos paying
names = input("Enter names seperated by commas: ")
names_list = names.split(",")
name_index_selected = random.randint(0, len(names_list) - 1)
print(f"{names_list[name_index_selected]} is going to buy lunch")

#tresure map challenge
row1 = ["😃","😃","😃"]
row2 = ["😃","😃","😃"]
row3 = ["😃","😃","😃"]

map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
choice = input("Input your treasure location: ")
map[int(choice[0])-1][int(choice[1])-1] = "x"
print(f"{row1}\n{row2}\n{row3}")


#final project: rock paper scisors game
rock = "🤘 rock"
paper = "✋ paper"
scisors = "🤞 scisors"


user_choice = int(input("Press 0 for rock, 1 for paper, 2 for scissors: "))
computer_choice = random.randint(0,2)

if user_choice >= 3 or user_choice < 0:
    print("Invalid input")
else:
    map = [rock, paper, scisors]
    user_choice_images = map[user_choice]
    computer_turn = map[computer_choice]

    if user_choice == 0 and computer_choice == 2:
        print(f"you choose {user_choice_images}")
        print(f"computer chooses {computer_turn}")
        print("you win")
    elif user_choice == 2 and computer_choice == 0:
        print(f"you choose {user_choice_images}")
        print(f"computer chooses {computer_turn}")
        print("computer wins")
    elif computer_choice > user_choice:
        print(f"you choose {user_choice_images}")
        print(f"computer chooses {computer_turn}")
        print("Computer wins")
    elif user_choice > computer_choice:
        print(f"you choose {user_choice_images}")
        print(f"computer chooses {computer_turn}")
        print("You win")
    else:
        print(f"you choose {user_choice_images}")
        print(f"computer chooses {computer_turn}")
        print("Game draw")




