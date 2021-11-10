# def greet_with(name, location):
#     print(f"hello {name}")
#     print(f"How is it like to live in {location}")
#
# # greet_with("denis", "kitale")
#
# #functions with keyword arguments
# greet_with(name="denis", location="Eldoret")

# #Area calc
# import math
# test_h = int(input("Enter height of the wall: "))
# test_w = int(input("Enter width of the wall: "))
# coverage = 5
# def paint_calc(height, width, cover):
#     no_of_cans = math.ceil((test_h * test_w) / coverage)
#     print(f"you will need {no_of_cans} cans of paint")
#
# paint_calc(height=test_h, width=test_w, cover=coverage)

#prime checker
# n = int(input("Check this number: "))
#
#
# def prime_check(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % 2 == 0:
#             is_prime = False
#     if is_prime:
#         print(f"{n} is  prime")
#     else:
#         print(f"{n} is not prime")
#
#
# prime_check(number=n)

# ceaser cypher project
proceed = True
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while proceed:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    def caesar(cipher_text, cipher_shift, cipher_direction):
        end_text = ""
        if direction == 'decode':
            cipher_shift *= -1
        for char in cipher_text:
            if char in alphabet:
                x = alphabet.index(char) + cipher_shift
                end_text += alphabet[x]
            else:
                end_text += char
        print(f"{direction}d result: {end_text}")


    caesar(cipher_text=text, cipher_shift=shift, cipher_direction=direction)
    next = input("do you need another operation: yes/no: ")
    if next == "yes":
        proceed = True
    else:
        proceed = False
        print("Good bye")
