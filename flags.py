import os

def run_flag_game():
    num_flags = 21

    rules_print()

    count = 1
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