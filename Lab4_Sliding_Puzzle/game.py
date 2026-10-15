import time
from puzzle import Puzzle


class SlidingPuzzle:
    SUPPORTED_SIZES = (3, 4, 5)

    def __init__(self, size=4):
        self.start_new_game(size)

    def start_new_game(self, size):
        if size not in self.SUPPORTED_SIZES:
            raise ValueError("Board size must be 3, 4, or 5.")
        self.size = size
        self.puzzle = Puzzle(self.size)
        self.moves = 0
        self.started = time.monotonic()
        self.completed = False

    def display(self):
        print()
        for row in self.puzzle.board:
            print(" ".join(f"{x or ' ':>2}" for x in row))
        print("Moves:", self.moves, " Time:", int(time.monotonic() - self.started), "s")

    def choose_size(self):
        while True:
            choice = input("Choose board size (3, 4, or 5): ").strip()
            try:
                size = int(choice)
            except ValueError:
                print("Please choose 3, 4, or 5.")
                continue
            if size in self.SUPPORTED_SIZES:
                return size
            print("Please choose 3, 4, or 5.")

    def run(self, size=None):
        if size is None:
            size = self.choose_size()
            self.start_new_game(size)
        elif size != self.size:
            self.start_new_game(size)
        print("Sliding Puzzle — W/A/S/D moves the tile into the blank. Q quits.")
        while not self.completed:
            self.display()
            if self.puzzle.solved():
                self.completed = True
                print("Solved!")
                break
            key = input("> ").strip().lower()
            if key == "q":
                return
            if key not in "wasd":
                print("Use W/A/S/D.")
                continue
            if self.puzzle.move(key):
                self.moves += 1
                print("Tile moved.")
            else:
                print("That move is not possible.")
