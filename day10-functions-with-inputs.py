#functions with outputs
# def format_name(f_name, l_name):
#     print(f_name.title())
#     l_name.title()
#
#
# format_name("denis", "DENIS")

#challenge days in months
#
# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
#
#
# def days_in_month(year, month):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if is_leap(year) and month == 2:
#         return 29
#     return month_days[month - 1]
#
#
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
#
# days = days_in_month(year, month)
# print(days)


#calculator project


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1/n2


calculator = dict()


calculator["+"] = add
calculator["-"] = subtract
calculator["*"] = multiply
calculator["/"] = divide

def calculate():
    num1 = float(input("What's the first number? "))
    for key in calculator:
        print(key)

    should_continue = True
    while should_continue:

        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("what's the next number? "))
        operation = calculator[operation_symbol]
        answer = operation(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input("Type y to continue calculation with the current answer or no to exit: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculate()


calculate()

