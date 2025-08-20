import random

print("Dice Roller")

while True:
    dice = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]

    roll = input("Roll the Dice? (y/n):").lower()

    if roll == "y":
        print("You rolled: ", random.choice(dice))

    else:
        break