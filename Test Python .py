def start_game():
    print("====================================")
    print("Welcome to the Dark Forest!")
    print("====================================")
    print("You wake up in a dense, foggy forest. You see two paths in front of you.")
    
    choice = input("Do you go 'left' toward the river, or 'right' toward the cave? ").lower()

    if choice == 'left':
        river_path()
    elif choice == 'right':
        cave_path()
    else:
        print("You stood still, getting lost in the fog. Game Over.")

# ==========================================
# DEVELOPER 1: FILL IN THE BLANKS INSIDE THE QUOTES
# ==========================================
def river_path():
    
    description = "You walk toward the rushing river..."
    
    option_1 = "Attempt to cross..."
    outcome_1 = "You try to step on the rocks, thinking they'd form a nice path, but you quickly slip and stumble, and now your clothes are all wet. Perhaps crossing was ill-advised..."
    
    option_2 = "Follow the course of the river..."
    outcome_2 = "After what feels like at least 10 minutes of walking, you come across what looks to be a miniature settlement deep in the brush..."
    
    # --- DO NOT EDIT BELOW THIS LINE ---
    print("\n" + description)
      print("1: " + option_1)
    print("2: " + option_2)
    ans = input("Do you choose 1 or 2? ")
    
    if ans == '1':
        print("\n" + outcome_1)
    elif ans == '2':
        print("\n" + outcome_2)
    else:
        print("\nYou didn't pick 1 or 2. Game Over.")


# ==========================================
# DEVELOPER 2: FILL IN THE BLANKS INSIDE THE QUOTES
# ==========================================
def cave_path():
    
    description = "You walk toward the dark, spooky cave..."
    
    option_1 = "Choose the tunnel to the left"
    outcome_1 = "There is a hungry beast waiting for a meal to come through"
    
    option_2 = "Choose the tunnel on the right"
    outcome_2 = "There ia a family of bats flying everywhere"
    
    # --- DO NOT EDIT BELOW THIS LINE ---
    print("\n" + description)
    print("1: " + option_1)
    print("2: " + option_2)
    ans = input("Do you choose 1 or 2? ")
    
    if ans == '1':
        print("\n" + outcome_1)
    elif ans == '2':
        print("\n" + outcome_2)
    else:
        print("\nYou didn't pick 1 or 2. Game Over.")


# This command starts the game (Do not edit)
start_game()


