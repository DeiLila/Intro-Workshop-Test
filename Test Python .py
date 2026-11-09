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
    
    option_1 = "Type the first choice here..."
    outcome_1 = "Type what happens if they pick the first choice..."
    
    option_2 = "Type the second choice here..."
    outcome_2 = "Type what happens if they pick the second choice..."
    
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
    
    option_1 = "Type the first choice here..."
    outcome_1 = "Type what happens if they pick the first choice..."
    
    option_2 = "Type the second choice here..."
    outcome_2 = "Type what happens if they pick the second choice..."
    
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


