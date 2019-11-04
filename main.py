import random


capitals = {"Croatia": "Zagreb", "Slovenia": "Ljubljana", "Austria": "Vienna", "Germany": "Berlin", "Poland": "Krakow",
            "The Netherlands": "Amsterdam", "Norway": "Oslo", "Denmark": "Copenhagen", "Sweden": "Stockholm",
            "Belgium": "Brussels", "Italy": "Rome", "France": "Paris", "England": "London",
            "Portugal": "Lisbon", "Spain": "Madrid"}

while True:

    lst = list(capitals.keys())

    print("Welcome to the Geography Quiz! Do you know the capitals of these 15 European countries?")

    score = 0

    while True:

        rand = random.choice(lst)
        answer = input("What is the capital of " + str(rand) + "? ")

        for key in capitals.keys():
            val = capitals[rand]

        if answer == val:
            score = score + 1
            print("That's correct! " + str(score) + "/15")
        else:
            score = score
            print("That's not correct. It's " + str(val) + ". " + str(score) + "/15")

        lst.remove(rand)
        if len(lst) == 0:
            break

    print("You have reached the end of the quiz! Your final score is " + str(score) + ".")
    end = input("Do you want to play again? ")

    if end == "yes":
        continue
    else:
        break
