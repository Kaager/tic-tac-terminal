import os
import subprocess
import sys
from flags import run_flag_game
from helpers import clear_cls

def main():

    columns, rows = os.get_terminal_size()
    #print(f"Columns (width): {columns}".center(columns))
    #print(f"Rows (height):   {rows}".center(columns))

    while True:
        clear_cls()
        main_menu()



def welcome_print() -> None:
    print("Welcome to Tic-Tac-Terminal")

def main_menu() -> None:
    print("--Main Menu--")
    print("1. Tic-Tac-Toe")
    print("2. 21 Flags - Bonus game")
    print("3. Exit")
    choice = int(input("Enter the digit of the option you want: "))

    if choice == 1:
        pass
    elif choice == 2:
        run_flag_game()
    elif choice == 3:
        sys.exit()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting gracefully. Goodbye!!!")
        sys.exit(0)
