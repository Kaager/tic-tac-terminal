import os
import sys
import random
from helpers import clear_cls, get_user_menu_choice

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
    
    choice = get_user_menu_choice(4)
            
    if choice == 1:
        pvp_mode(num_flags)
    elif choice == 2:
        choose_pve_difficulty(num_flags)
    elif choice == 3:
        return False
    elif choice == 4:
        sys.exit(0)
    
    return True


def choose_pve_difficulty(num_flags: int) -> None:
    clear_cls()
    rules_print()
    print("--Choose difficulty--")
    print("1. Normal")
    print("2. Hard")
    print("3. Impossible")
    print("4. Back")

    user_choice = get_user_menu_choice(4)

    if user_choice == 1:
        pve_normal(num_flags)
    elif user_choice == 2:
        pve_hard(num_flags)
    elif user_choice == 3:
        pve_impossible(num_flags)
    elif user_choice == 4:
        pass


def pve_hard(num_flags: int) -> None:
    player: str = ""
    count: int = get_starting_player()
    clear_cls()
    rules_print()
    while num_flags > 0:
        draw_flags(num_flags)
        if count % 2 == 1:
            player = "Player"
            player_input = get_user_game_input(player)
            num_flags -= player_input
        elif count % 2 == 0:
            player = "Bot"
            if num_flags > 16:
                bot_choice = random.randint(1, 3)
            else:
                bot_choice = num_flags % 4
                bot_choice = max(bot_choice, 1)
            num_flags -= bot_choice
            print(f"Bot chose to remove {bot_choice} flag(s)")
        count += 1
        separator_print()
    print(f"{player} wins!!!")
    input("Press Enter to continue...")


def pve_impossible(num_flags: int) -> None:
    player: str = ""
    count: int = 2 # set starting player to the bot
    clear_cls()
    rules_print()
    while num_flags > 0:
        draw_flags(num_flags)
        if count % 2 == 1:
            player = "Player"
            player_input = get_user_game_input(player)
            num_flags -= player_input
        elif count % 2 == 0:
            player = "Bot"
            bot_choice = num_flags % 4
            bot_choice = max(bot_choice, 1)
            num_flags -= bot_choice
            print(f"Bot chose to remove {bot_choice} flag(s)")
        count += 1
        separator_print()
    print(f"{player} wins!!!")
    input("Press Enter to continue...")

def pve_normal(num_flags: int) -> None:
    player: str = ""
    count: int = get_starting_player()
    clear_cls()
    rules_print()
    while num_flags > 0:
        draw_flags(num_flags)
        if count % 2 == 1:
            player = "Player"
            player_input = get_user_game_input(player)
            num_flags -= player_input
        elif count % 2 == 0:
            player = "Bot"
            if num_flags <= 3:
                bot_choice = 3
            elif num_flags == 4:
                bot_choice = 1
            elif num_flags == 5:
                bot_choice= 1
            elif num_flags == 6:
                bot_choice = 2
            elif num_flags == 7:
                bot_choice = 3
            else:
                bot_choice = random.randint(1, 3)
            print(f"Bot chose to remove {bot_choice} flag(s)")
            num_flags -= bot_choice
        count += 1
        separator_print()

    print(f"{player} wins!!!")
    input("Press Enter to continue...")

def get_starting_player() -> int:
    clear_cls()
    rules_print()
    print("--Who will go first?--")
    print("1. Player (you)")
    print("2. Bot")
    print("3. Random")

    choice = get_user_menu_choice(3)

    if choice == 1:
        return 1
    elif choice == 2:
        return 2
    else:
        return random.randint(1, 2)


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
    input("Press Enter to continue...")

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