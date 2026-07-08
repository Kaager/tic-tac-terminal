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
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "],
    ]

    while True:
        ttt_board_print(board)
        player_choice = get_user_menu_choice(9)
        place_choice_on_board(player_choice, "X", board)


def place_choice_on_board(choice: int, icon: str, board: list[list[str]]) -> None:
    # need something to check if the field is non-empty
    row: int = (choice - 1) // len(board)
    column: int = (choice -1) % len(board)
    board[row][column] = icon



def ttt_board_print(board: list[list[str]]) -> None:
    sep_pieces: list[str] = ["---"] * len(board)
    seperator: str = "+".join(sep_pieces)

    print()
    for i, row in enumerate(board):
        row_str = " | ".join(row)
        print(" " + row_str + " ")
        if i != len(board) - 1:
            print(seperator)
    print()
