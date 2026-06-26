import os

def run_flag_game():
    rules_print()
    draw_flags(21)

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
    print(display)