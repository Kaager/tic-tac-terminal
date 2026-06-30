import subprocess
import os


def clear_cls():
    # clear terminal, choose correct command based on os.name
    # which will be nt for windows, and posix for linux/macos
    # soft deprecate: os.system("cls" if os.name == "nt" else "clear")
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)