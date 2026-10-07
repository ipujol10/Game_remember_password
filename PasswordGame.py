"""Main game loop"""

from PasswordGameIpujol10.Game import Game


def main() -> None:
    """Entry program"""
    with Game() as g:
        g.mainloop()


if __name__ == "__main__":
    main()
