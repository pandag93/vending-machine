foods = []
sweet1 = {"ID": "1", "Name": "haribles", "Calories": 380, "Weight": 15} #weight in grams, calories per 100g
sweet2 = {"ID": "2", "Name": "choco bar", "Calories": 450, "Weight": 57}
savoury1 = {"ID": "3", "Name": "bag of popcorn", "Calories": 485, "Weight": 18}

foods.append(sweet1)
foods.append(sweet2)
foods.append(savoury1)
print(foods)

#here's the option
for food in foods:
    message = "{ID}. You can choose {Name}, that has {Calories} calories per 100 grams and has a serving size of {Weight} grams.".format(**food)
    print(message)

#choose a food
print("Which would you like?")
choice = input()
chosenFood = None
for food in foods:
    if food ["ID"] == choice:
        chosenFood = food
calsPerServ = chosenFood["Calories"] / 100 * chosenFood["Weight"]
print("You have chosen {} , and it has {} calories per serving.".format(chosenFood["Name"], calsPerServ))
print("Are you sure you want this food? Please answer Y/N")
finalChoice = input().capitalize()
if finalChoice == "Y":
    print("Here you go, here's a {}!".format(chosenFood["Name"]))
elif finalChoice == "N":
    print("You probably don't need that {} anyway...".format(chosenFood["Name"]))
else:
    print("Sorry, I only understand Y or N! Try again!")