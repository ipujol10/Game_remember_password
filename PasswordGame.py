"""Main game loop"""

from Game_Remember_Password.Game import Game


def main() -> None:
    """Entry program"""
    with Game() as g:
        g.mainloop()


if __name__ == "__main__":
    main()
