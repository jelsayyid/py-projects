
# Choose Your Own Adventure: The Mystical Forest Adventure

def endowment_question():
    print("You notice that Yale is raising money for its global mission for public service and education.")
    endowment_choice = input("\nDo you wish to donate? (y/n)")

def adventure_game():
    print("Welcome to the Yale Mystical Forest Adventure!")
    print("You are an explorer seeking the legendary treasure hidden deep within the forest.\n")
    print("But, be aware, bold student. There are rumors of...well...better not to spook ya\n")

    first_choice = input("As you enter the forest, you come to a fork in the path. Do you go left or right? (left/right): ").lower()
    if first_choice == "left":
        print("\nYou've chosen the left path and encounter a mysterious old bridge.")
        bridge_choice = input("Do you cross the bridge or head back? (cross/back): ").lower()
        if bridge_choice == "cross":
            print("\nYou bravely cross the bridge and find the treasure! Congratulations, you've won the game!")
            endowment_choice = input("\nDo you want to share the treasure to support Yale's endowment? (y/n)")
        else:
            print("\nYou decide to head back and exit the forest. Maybe next time you'll find the treasure.")
    else:
        print("\nYou've chosen the right path and come across a sleeping dragon.")
        dragon_choice = input("Do you try to sneak past the dragon or turn around? (sneak/turn): ").lower()
        if dragon_choice == "sneak":
            print("\nYou successfully sneak past the dragon, but unfortunately, the path leads to a dead end.")
            print("You decide to return another day to continue your search for the treasure.") 
            endowment_question()
        else:
            print("\nYou turn around and exit the forest, deciding that today is not the day to face a dragon.")

    print("\nThank you for playing the Mystical Forest Adventure!")
    if endowment_choice == "y":
        print("\nWe value your support to Yale's global mission")
    else:
        print("\nDo consider being more generous in the future!")

# Running the game
# Since input() function is used, the game requires user input.
adventure_game()
