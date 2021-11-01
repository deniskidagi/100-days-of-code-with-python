#conditional statements, logical operators code blocks and scope

#exercise: check whether a given number is even or odd
# num = int(input("Enter number? "))
# if num % 2 == 0:
#     print("number is even")
# else:
#     print("Number is odd")
#
#
#exercise: bmi calculator2
# weight = float(input("Enter weight? "))
# height = float(input("Enter height? "))
#
# bmi = (weight / (height ** 2))
# print(f"bmi is {bmi}")
# if bmi > 18.5:
#     if bmi > 35:
#         print("You are clinically obese")
#     elif bmi > 30:
#         print("You are obese")
#     elif bmi > 25:
#         print("Yoe are overweight")
#     else:
#         print("you have a normal weight")
#
# else:
#     print("You are underweight")

#leap year
# year = int(input("Enter year"))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year")
#         else:
#             print("Not leap year")
#     else:
#         print("Leap year")
# else:
#     print("Not leap year")

#challenge: automatic pizza order program
# print("Welcome to our pizza offers")
# size = input("Input size of pizza: S for small, L for large, M for medium")
# toppings = input("Do you also need the pizza toppings?: y/n")
# cheese = input("We also offer cheese would you like too check it out? y/n")
# total_price = 0
# top_small = 2
# top_medium_large = 3
# extra_cheese = 1
# if size == "s":
#     if toppings == "y":
#         total_price = 15 + top_small
#     elif cheese == "y":
#         total_price = 15 + top_small + 2
#     else:
#         total_price = 15
#
# elif size == "m":
#     if toppings == "y":
#         total_price = 20 + top_medium_large
#     elif cheese == "y":
#         total_price = 20 + top_medium_large + 1
#     else:
#         total_price = 20
#
# elif size == "l":
#
#     if toppings == "y":
#         total_price = 25 + top_medium_large
#     elif cheese == "y":
#         total_price = 25 + top_medium_large + 1
#     else:
#         total_price = 25
#
# else:
#     print("Request not available")
#
#
# print(f"Your total bill is {total_price}")

#challenge: love calculator
# your_name = input("Enter your name: ")
# their_name = input("Enter their name: ")
#
# combined_name = your_name + their_name
# t = combined_name.count("t")
# r = combined_name.count("r")
# u = combined_name.count("u")
# e = combined_name.count("e")
# total_true = t + r + u + e
#
# l = combined_name.count("l")
# o = combined_name.count("0")
# v = combined_name.count("v")
# e = combined_name.count("e")
#
# total_love = l + o + v + e
#
# lovescore = str(total_true) + str(total_love)
# total_lovescore = int(lovescore)
#
# if total_lovescore < 10 or total_lovescore > 90:
#     print(f"Your score is {total_lovescore} you together like coke and mentos")
# elif 40 < total_lovescore < 50:
#     print(f"Your score is {total_lovescore} you are alright together")
# else:
#     print(f"your love score is {total_lovescore}")


#final project: treasure island
print("Welcome to the treasure game: ")
print("Your mission is to find your treasure:")
print('''
#########################################################################################################
      _        _
      /\\     ,'/|
       _|  |\-'-'_/_/
  __--'/`           \
      /              \
     /        "o.  |o"|
     |              \/
      \_          ___\
        `--._`.   \;//
             ;-.___,'
            /
          ,'
       _-'
#########################################################################################################
''')

direction = input("You are out of your door. where are you wanna go: left or right")
if direction == "left":
    cross_river = input("You are across the river, do you want to swim or wait for boat? : swim or wait")
    if cross_river == "wait":
        door = input("Choose door to enter? red, blue, yellow")
        if door == "yellow":
            print("Congratulations you have won the game")
        else:
            if door == "blue":
                print("Eaten by beasts, game over")
            elif door == "red":
                print("burned with fire, game over")
            else:
                print("game over")
    else:
        print("Attacked by crocodile game over")

else:
    print("game over")


