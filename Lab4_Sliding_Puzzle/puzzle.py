import random


class Puzzle:
    def __init__(self, size=4):
        self.size = size
        self.board = self.make_board()

    def make_board(self):
        tiles = list(range(1, self.size * self.size)) + [0]
        self.board = [
            tiles[r * self.size:(r + 1) * self.size] for r in range(self.size)
        ]

        directions = ("w", "a", "s", "d")
        deltas = {"w": (-1, 0), "s": (1, 0), "a": (0, -1), "d": (0, 1)}
        opposite = {"w": "s", "a": "d", "s": "w", "d": "a"}
        previous_move = None
        scramble_moves = max(20, self.size * self.size * 10)

        for _ in range(scramble_moves):
            blank_row, blank_column = self.blank_pos()
            legal_moves = [
                direction
                for direction in directions
                if (
                    0 <= blank_row + deltas[direction][0] < self.size
                    and 0 <= blank_column + deltas[direction][1] < self.size
                )
            ]
            if previous_move is not None and len(legal_moves) > 1:
                legal_moves.remove(opposite[previous_move])

            direction = random.choice(legal_moves)
            self.move(direction)
            previous_move = direction

        if self.size > 1 and self.solved():
            blank_row, blank_column = self.blank_pos()
            legal_moves = [
                direction
                for direction in directions
                if (
                    0 <= blank_row + deltas[direction][0] < self.size
                    and 0 <= blank_column + deltas[direction][1] < self.size
                )
            ]
            if previous_move is not None and len(legal_moves) > 1:
                legal_moves.remove(opposite[previous_move])
            self.move(random.choice(legal_moves))

        return self.board

    def blank_pos(self):
        for r in range(self.size):
            for c in range(self.size):
                if self.board[r][c] == 0:
                    return r, c

    def move(self, direction):
        r, c = self.blank_pos()
        dr, dc = {"w": (-1, 0), "s": (1, 0), "a": (0, -1), "d": (0, 1)}[direction]
        nr, nc = r + dr, c + dc
        if not (0 <= nr < self.size and 0 <= nc < self.size):
            return False
        self.board[r][c], self.board[nr][nc] = self.board[nr][nc], self.board[r][c]
        return True

    def solved(self):
        return sum(self.board, []) == list(range(1, self.size * self.size)) + [0]
