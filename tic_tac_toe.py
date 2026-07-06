import sys
from helpers import clear_cls, get_user_menu_choice


def run_tic_tac_toe() -> None:
    run_ttt = True
    while run_ttt:
        clear_cls()
        run_ttt = ttt_menu()


def ttt_menu() -> bool:
    print("--Menu--")
    print("1. PvP")
    print("2. PvE")
    print("3. Main Menu")
    print("4. Quit")

    choice = get_user_menu_choice(4)

    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        return False
    elif choice == 4:
        sys.exit(0)

    return True
