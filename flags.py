import os
import sys
from helpers import clear_cls

def run_flag_game():
    num_flags = 21
    run_flags_menu: bool = True
    while run_flags_menu:
        clear_cls()
        rules_print()
        run_flags_menu = flags_menu(num_flags)

def flags_menu(num_flags: int) -> bool:
    print("--Menu--")
    print("1. PvP")
    print("2. PvE")
    print("3. Main Menu")
    print("4. Quit")
    
    choice = get_user_menu_input(4)
            
    if choice == 1:
        pvp_mode(num_flags)
    elif choice == 2:
        choose_pve_difficulty(num_flags)
    elif choice == 3:
        return False
    elif choice == 4:
        sys.exit(0)
    
    return True


def get_user_menu_input(num_menu_options: int):
    choice = ""
    avail_options = []
    for i in range(num_menu_options):
        avail_options.append(i+1)

    user_input_correct = False
    while not user_input_correct:
        choice = input("Enter the digit for the option you want: ")
        try:
            choice = int(choice)
        except ValueError:
            print("Please choose a valid option!")

        if choice in avail_options:
            user_input_correct = True
        else:
            print("Please choose a valid option!")
    return choice


def choose_pve_difficulty(num_flags: int) -> None:
    clear_cls()
    rules_print()
    print("--Choose difficulty--")
    print("1. Normal")
    print("2. Hard")
    print("3. Impossible")
    print("4. Back")

    user_choice = get_user_menu_input(4)

    if user_choice == 1:
        pass
    elif user_choice == 2:
        pass
    elif user_choice == 3:
        pass
    elif user_choice == 4:
        pass



def pvp_mode(num_flags: int) -> None:
    player: str = ""
    count: int = 1
    while num_flags > 0:
        if count % 2 == 1:
            player = "Player_1"
        elif count % 2 == 0:
            player = "Player_2"
        draw_flags(num_flags)
        player_input = get_user_game_input(player)
        num_flags -= player_input
        count += 1
        separator_print()
    print(f"{player} wins!!!")
    _ = input()


def rules_print() -> None:
    rules = """21 FLAGS
Rules:
There are 21 flags. Players take turns removing 1, 2, or 3 flags. The player who takes the last flag wins.
"""
    columns, _ = os.get_terminal_size()
    for line in rules.splitlines():
        print(line.center(columns))
    
    separator_print()


def separator_print(separator: str = "-") -> None:
    columns, _ = os.get_terminal_size()
    print(separator * columns)


def draw_flags(count: int) -> None:
    groups = count // 5
    remainder = count % 5
    display = ("||||| " * groups) + ("|" * remainder)
    print(f"Flags remaining: {count}")
    print(display)


def get_user_game_input(player: str) -> int:
    p_input = input(f"{player}: ")

    try:
        pi_input = int(p_input)
    except ValueError:
        print("Value must be 1, 2 or 3. Please try again!")
        return get_user_game_input(player)

    if pi_input not in (1, 2, 3):
        print("Value must be 1, 2 or 3. Please try again!")
        return get_user_game_input(player)
    
    return pi_input