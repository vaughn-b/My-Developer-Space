# This is a dice guessing game
# Je'Vaughn Black
# ITP100-03WA
# Exercise 06B
# dice01jb.py


import random

d6Pair1 = random.randint(1, 6) + random.randint(1, 6)
d6Pair2 = random.randint(1, 6) + random.randint(1, 6)
d6Pair3 = random.randint(1, 6) + random.randint(1, 6)

print("""My Dice Game .v01
You have three rolls of the dice to match a number you select.
Good luck!!""")
print("-" * 63)

while True:
    try:
        guess = int(input("Choose a number between 2 and 12: "))
        while 2 > guess or 12 < guess:
            guess = int(input("Choose a number between 2 and 12: "))
        break
    except ValueError:
        print
if 2 <= guess <= 12:
    for diceRoll in range(1, 2):
        print(f"Dice Roll #{diceRoll} is {d6Pair1}")
        if d6Pair1 != guess:
            for diceRoll2 in range(2, 3):
                print(f"Dice Roll #{diceRoll2} is {d6Pair2}")
                if d6Pair2 != guess:
                    for diceRoll3 in range(3, 4):
                        print(f"Dice Roll #{diceRoll3} is {d6Pair3}")
                        if d6Pair3 != guess:
                            print("You Lose!!")

if d6Pair1 == guess or d6Pair2 == guess or d6Pair3 == guess:
    print("You Win!!")
