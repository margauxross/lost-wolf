## Tutorial stage for the game

print("You are in a bright room.")
print("You can go north, south, and west.")
print("You hear a gurgling in the distance.")

print("Choose an action:\n")
action_input = input('Action: ')

if action_input == "south":
    print("The gurgling grows louder. Ominous.")
    print("the brightness intensifies")
    print("on the ground before you, you see running water")
    print("you can inspect water, jump in water, west, or do nothing")
    print("choose an action")
    action_input = input('Action: ')
    if action_input == "inspect water":
        print("a shimmering face peers at you, a reflection wildly different from your own.")
    elif action_input == "jump in water":
        print("you are now wet.")
    elif action_input == "do nothing":
        print("nothing happens.")
    elif action_input == "west":
        number_rocks = 0
        print("""You fall through a hole and find yourself in a white, 
                    featureless room with rocks scattered on the ground""")
        while number_rocks < 3:

            print("You have ", number_rocks, " rocks")
            action_input = input('Action: ')

            if action_input == "pick up rock":
                number_rocks = number_rocks + 1
            else:
                print("You cannot do that.")
            if number_rocks == 3:
                print("An old man materializes before you and bows. He takes the rocks from your hands, smiles, and disappears")
                number_rocks = 0
elif action_input == "north":
    print("It is very dark. You are eaten by a grue.")
elif action_input == "west":
    print(
        "a great gust of wind rises through the vent in the floor- spinning you around until you are back where you started.")
else:
    print("You cannot do that:", action_input)

