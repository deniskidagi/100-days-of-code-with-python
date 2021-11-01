#data types

#strings
# print("hello"[0])
# print("hello"[4])

#challenge
# num = 45
# x = str(num)
# y = x[0]
# z = x[1]
# sum = int(y)+ int(z)
# print(sum)

# #BMI calculator challenge
# height = float(input("Enter height? "))
# weight = float(input("Enter weight? "))
#
# bmi = (height / (weight * weight))
# print(round(bmi))
#

#exercise life in weeks
# age = int(input("What is your age? "))
# years = 90 - age
# weeks = years * 52
# days = years * 365
# print(f"You are left with {weeks} weeks and {days} days to reach 90 years")

#final project tip calculator
print("Welcome to the tip calculator")
bill = float(input("What was the total bill? "))
percentage_tip = int(input("What percentage tip would you like to give 10, 12 or 15? "))
# if percentage_tip == 10:
#     percentage_tip = 1 + (10 / 100)
#
# elif percentage_tip == 12:
#     percentage_tip = 1 + (12 / 100)
#
# else:
#     percentage_tip = 1 + (15 / 100)

total_amount = ((percentage_tip / 100) + 1) * bill
number_of_people = int(input("How many people to split the bill? "))

total_pay = (total_amount / number_of_people)
print("{:.2f}".format(total_pay))