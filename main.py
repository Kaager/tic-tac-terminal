import os
import sys
from flags import run_flag_game

def main():

    columns, rows = os.get_terminal_size()
    #print(f"Columns (width): {columns}".center(columns))
    #print(f"Rows (height):   {rows}".center(columns))

    while True:
        clear_cls()
        main_menu()

def clear_cls():
    # clear terminal, choose correct command based on os.name
    # which will be nt for windows, and posix for linux/macos
    os.system("cls" if os.name == "nt" else "clear")

def welcome_print() -> None:
    print("Welcome to Tic-Tac-Terminal")

def main_menu() -> None:
    print("--Menu--")
    print("1. Tic-Tac-Toe")
    print("2. 21 Flags - Bonus game")
    print("3. Exit")
    choice = int(input("Enter the digit of the option you want: "))

    if choice == 1:
        pass
    elif choice == 2:
        clear_cls()
        run_flag_game()
    elif choice == 3:
        sys.exit()

if __name__ == "__main__":
    main()
