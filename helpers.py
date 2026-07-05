import subprocess
import os


def clear_cls():
    # clear terminal, choose correct command based on os.name
    # which will be nt for windows, and posix for linux/macos
    # soft deprecate: os.system("cls" if os.name == "nt" else "clear")
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)


def get_user_menu_choice(num_menu_options: int) -> int:
    avail_options = list(range(1, num_menu_options + 1))
    while True:
        choice = input("Enter the digit for the option you want: ")
        try:
            choice = int(choice)
        except ValueError:
            print("Please choose a valid option!")
            continue # skip the following check

        if choice in avail_options:
            break
        else:
            print("Please choose a valid option!")
    return choice