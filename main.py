import os
from flags import run_flag_game

def main():
    clear_cls()

    columns, rows = os.get_terminal_size()
    #print(f"Columns (width): {columns}".center(columns))
    #print(f"Rows (height):   {rows}".center(columns))

    run_flag_game()

def clear_cls():
    # clear terminal, choose correct command based on os.name
    # which will be nt for windows, and posix for linux/macos
    os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    main()
