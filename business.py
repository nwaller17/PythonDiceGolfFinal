import random
from db import display_scores
def play_game():
    total_strokes = 0
    for hole in range(1, 10):
        distance_remaining = random.randint(350, 500) # Randomly generates the distance to the hole at the start
        print(f"\nHole {hole}: Distance is {distance_remaining} yards.")
        strokes_for_hole = 0

        while distance_remaining > 0:
            swing_type = choose_swing_type()
            dice_roll = roll_dice()
            max_roll = min(dice_roll, 4)
            strokes_for_hole += 1
            
            distance_hit = swing_type * max_roll
            distance_remaining = max(0, distance_remaining - distance_hit) # Prevents distance remaining from returning negative values
            
            if dice_roll == 5 and swing_type == 70: # Sand trapped on hard swing
                strokes_for_hole += 1
                print("You got stuck in the bunker and wasted a stroke getting out!")
            elif dice_roll == 5 and swing_type == 50: # Sand trapped on normal swing
                strokes_for_hole += 1
                print("You got stuck in the bunker and wasted a stroke getting out!")
            elif dice_roll == 6 and swing_type == 70: # Water penalty
                strokes_for_hole += 1
                print("Splash! +1 stroke for a water penalty.")

            print(f"You rolled a {dice_roll}!")
            print(f"Hit distance: {distance_hit} yards (Swing Type: {swing_type} * Dice Multiplier (Max 4): {max_roll}).")
            print(f"Remaining distance to hole: {distance_remaining} yards.")
            print(f"Strokes for this hole: {strokes_for_hole}.")
            
            if distance_remaining <= 0:
                print("Nice shot! Moving on to the next hole.")
                break
        
        total_strokes += strokes_for_hole
        print(f"Total strokes after Hole {hole}: {total_strokes}.")
        
    print(f"Total strokes for all holes: {total_strokes}.")
    print("Comparing your score with professional golfers' scores:")
    display_scores()

def choose_swing_type():
    print("Choose your swing type: 1. Soft 2. Normal 3. Hard")
    choice = input("Enter your choice: ")
    if choice == '1':
        return 30 # Soft swing multiplier
    elif choice == '2':
        return 50 # Normal swing multiplier
    elif choice == '3':
        return 70 # Hard swing multiplier
    else:
        print("Was that a trickshot attempt? Defaulting to Normal swing.")
        return 50

def roll_dice():
    return random.randint(1, 6) # Simulates a dice roll for random value between 1 and 6
