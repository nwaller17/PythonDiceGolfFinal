import random
import sqlite3
from business import play_game
from db import display_scores

def main_menu():
    print("""Welcome to the Golf Pro Challenge! 
Take on the greatest golfers in the world on a challenging
course with sand traps and pools of water around every corner. 
Choose your swing type and roll the dice to calculate your hit distance, 
but don't swing too hard! Normal and Hard swings that roll a 5 as well as 
Hard swings that roll a 6 could land you on the beach. 
Best of luck!""")
    
    while True:
        print("\nMenu:")
        print("Press 1 to preview the competitions scores.")
        print("Press 2 to begin the game.")
        print("Press 3 to exit.")
        choice = input("Enter your choice: ")

        if choice == '1':
            display_scores()
        elif choice == '2':
            play_game()
            play_again = input("Do you want to play again? (y/n): ").lower()
            if play_again != 'y':
                print("Thank you for playing!")
                break
        elif choice == '3':
            print("Thank you for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
