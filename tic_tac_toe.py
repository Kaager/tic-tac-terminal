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
        pvp_mode()
    elif choice == 2:
        pass
    elif choice == 3:
        return False
    elif choice == 4:
        sys.exit(0)
    return True


def pvp_mode() -> None:
    board: list[list[str]] = [
        ["X", "x", " "],
        ["O", "o", "0"],
        ["0", "X", "0"],
    ]

    ttt_board_print(board)
    input("Press Enter to continue...!")

def ttt_board_print(board: list[list[str]]) -> None:
    row_num: int = 0
    final_board_size: int = len(board) * 2 - 1
    sep_pieces: list[str] = ["---"] * len(board)
    seperator: str = "+".join(sep_pieces)

    print()    
    for i in range(final_board_size):
        if i % 2 == 0:
            row_str = " | ".join(board[row_num])
            row_num += 1
            print(" " + row_str + " ")
        if i % 2 == 1:
            print(seperator)
    print()
