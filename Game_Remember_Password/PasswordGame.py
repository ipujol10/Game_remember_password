"""Main game loop"""

from Game import Game


def main() -> None:
    """Entry program"""
    with Game() as g:
        g.mainloop()


if __name__ == "__main__":
    main()
