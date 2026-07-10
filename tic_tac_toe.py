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
    print("4. How to play")
    print("5. Quit")

    choice = get_user_menu_choice(5)

    if choice == 1:
        pvp_mode()
    elif choice == 2:
        pass
    elif choice == 3:
        return False
    elif choice == 4:
        how_to_play()
    elif choice == 5:
        sys.exit(0)
    return True


def pvp_mode() -> None:
    board: list[list[str]] = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "],
    ]
    player1_icon = "X"
    player2_icon = "O"
    turn_count = 1

    while True:
        clear_cls()
        ttt_board_print(board)
        if turn_count % 2 == 1:
            player = f"Player 1 ({player1_icon})"
            icon = player1_icon
        elif turn_count % 2 == 0:
            player = f"Player 2 ({player2_icon})"
            icon = player2_icon
        print(player)
        player_choice = get_user_menu_choice(9)
        place_choice_on_board(player_choice, icon, board)

        turn_count += 1


def place_choice_on_board(choice: int, icon: str, board: list[list[str]]) -> None:
    # need something to check if the field is non-empty
    row: int = (choice - 1) // len(board)
    column: int = (choice -1) % len(board)
    board[row][column] = icon


def how_to_play() -> None:
    ref_board = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]
    ]
    how_to = """--How to play--
To place your piece, enter the digit for the corresponding field. The fields are numbered like this:"""
    clear_cls()
    print(how_to)
    ttt_board_print(ref_board)
    input("Press Enter to continue...!")


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
