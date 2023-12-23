
# Choose Your Own Adventure: The Mystical Forest Adventure

def adventure_game():
    print("Welcome to the Yale Mystical Forest Adventure!")
    print("You are an explorer seeking the legendary treasure hidden deep within the forest.\n")

    first_choice = input("As you enter the forest, you come to a fork in the path. Do you go left or right? (left/right): ").lower()
    if first_choice == "left":
        print("\nYou've chosen the left path and encounter a mysterious old bridge.")
        bridge_choice = input("Do you cross the bridge or head back? (cross/back): ").lower()
        if bridge_choice == "cross":
            print("\nYou bravely cross the bridge and find the treasure! Congratulations, you've won the game!")
        else:
            print("\nYou decide to head back and exit the forest. Maybe next time you'll find the treasure.")
    else:
        print("\nYou've chosen the right path and come across a sleeping dragon.")
        dragon_choice = input("Do you try to sneak past the dragon or turn around? (sneak/turn): ").lower()
        if dragon_choice == "sneak":
            print("\nYou successfully sneak past the dragon, but unfortunately, the path leads to a dead end.")
            print("You decide to return another day to continue your search for the treasure.")
        else:
            print("\nYou turn around and exit the forest, deciding that today is not the day to face a dragon.")

    print("\nThank you for playing the Mystical Forest Adventure!")

# Running the game
# Since input() function is used, the game requires user input.
adventure_game()
