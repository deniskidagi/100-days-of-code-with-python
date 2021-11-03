fruits = ["apple","mango","oranges","banana"]
for i in fruits:
    print(i)
    print(i + "pie")
print(fruits)

#exercise: calculate average heights of students
students_list = input("Enter students heights: ").split(",")
students = []
sum = 0
total = 0
for i in students_list:
    i  = int(i)
    students.append(i)
for i in students:
    sum += i
    total += 1
average = round(sum / total)
print(f"Average is {average}")

# using sum and len function
students_list = input("Enter students heights: ").split(",")
students = []
for i in students_list:
    i  = int(i)
    students.append(i)
average = round(sum(students) / len(students))
print(f"average {average}")

#challenge highest score
students_scores = input("Enter students scores seperated by comma: ").split(",")
largest = 0
for i in range(0, len(students_scores)):
    students_scores[i] = int(students_scores[i])
    if(students_scores[i] > largest):
        largest = students_scores[i]

print(largest)

#for loops and the range function
total = 0
for i in range(1, 101):
    total += i
print(total)
#challenge: add even numbers
total = 0
for i in range(0, 101, 2):
    total += i
print(total)

#challenge fizzbuzz
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)

#final project: password generator
import random
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
           "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M" ,"N",
           "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

numbers = ["0", "2", "3", "4", "5", "6", "7", "8", "9"]

symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("welcome to pyPassword generator: ")
in_letters = int(input("How many letters for your password:\n"))
in_numbers = int(input("How many numbers for your password:\n"))
in_symbols = int(input("How many symbols for your password:\n"))

password_list = []
for char in range(0, in_letters):
    password_list.append(random.choice(letters))
for char in range(0, in_numbers):
    password_list.append(random.choice(numbers))
for char in range(0, in_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)
password = ""
for i in password_list:
    password += i
print(f"generated password is: {password}")


