"""A simple game to help remembering passwords"""
import getpass
from enum import Enum


class Colors(Enum):
    """
    Enum for the colors codes
    """

    RESET = "0"
    BOLD = "1"
    ITALIC = "3"
    UNDER = "4"
    RED = "31"
    GREEN = "32"
    YELLOW = "33"


def format_txt(text: str, color: list[Colors]) -> str:
    """
    Format the text with the different options/colors
    """
    mods: str = ""
    for mod in color:
        mods += mod.value + ";"
    return f"\033[{mods[:-1]}m{text}\033[{Colors.RESET.value}m"


def diff(password: str, guess: str) -> str:
    """
    Return the string with the missed characters
    """
    length: int = max(len(password), len(guess))
    out: str = ""
    for i in range(length):
        if i >= len(password):
            out += format_txt("x", [Colors.YELLOW, Colors.UNDER])
        elif i >= len(guess):
            out += format_txt("?", [Colors.YELLOW, Colors.UNDER])
        else:
            color: Colors = Colors.RESET
            if password[i] == guess[i]:
                color = Colors.GREEN
            else:
                color = Colors.RED
            out += format_txt(guess[i], [color])
    return out


def main() -> None:
    """
    Main program
    """
    password: str = getpass.getpass(prompt="Correct password: ")

    guess: str = getpass.getpass(prompt="Guess: ")
    while guess != password:
        print("Incorrect password")
        print(diff(password, guess))

        guess = getpass.getpass(prompt="Guess: ")


if __name__ == "__main__":
    main()
