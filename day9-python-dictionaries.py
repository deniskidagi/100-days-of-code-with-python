#dictionaries deep dive
programming_dictionary = {
    "bug": "An error in a program",
    "function": "A piece of code that you can easily call over and over again",
}
programming_dictionary["loop"] = "The action of doing something over and over again"

#create an empty dictionary
empty_dictionary = {}

#loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

#grading program
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermion": 99,
    "Draco": 74,
    "Nevill": 62
}
#create an empty dictionary called student grade
student_grade = {}
for key in student_scores:
    score = student_scores[key]
    if score > 90:
        student_grade[key] = "Outstanding"
    elif score > 80:
        student_grade[key] = "Exceeds expectation"
    elif score > 70:
        student_grade[key] = "Acceptable"
    else:
        student_grade[key] = "Fail"

print(student_grade)

#nesting lists and dictionaries
travel_log =[
    {
        "country": "France",
        "cities_visited": ["paris", "lille", "dijong"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "humberg", "startgut"],
        "total_visits": 12
    }]
def add_travel_log(name, visits, cities=[]):
    newDict = {
        "country": name,
        "cities_visited": cities,
        "total_visits": visits
    }
    travel_log.append(newDict)

add_travel_log("kenya", 2, ["Nairobi", "Kitale", "Eldoret"])
print(travel_log)

#auction bid game
def clear():
    import os
    os.system("clear")


bids = {}

bidding_finished = False


def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} and bid is {highest_bid}")


while not bidding_finished:
    name = input("What is your name? ")
    price = int(input("What is your bid? $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? ")
    if should_continue == "no":
        bidding_finished = True
        highest_bidder(bids)
    elif should_continue == "yes":
        clear()