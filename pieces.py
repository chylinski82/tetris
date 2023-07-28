import random

from board import Board

class Piece:
    # The SHAPES constant represents all possible shapes a piece can take
    SHAPES = [
        [
            ['🂠'],
            ['🂠'],
            ['🂠'],
            ['🂠'],
        ],
        [
            ['🂠', '🂠'],
            ['🂠', '🂠'],
        ],
        [
            [' ', '🂠'],
            ['🂠', '🂠'],
            ['🂠', ' '],
        ],
        [
            ['🂠', ' '],
            ['🂠', '🂠'],
            [' ', '🂠'],
        ],
        [
            ['🂠', '🂠', '🂠'],
            [' ', '🂠', ' '],
        ],
        [
            ['🂠', '🂠', '🂠'],
            ['🂠', ' ', ' '],
        ],
        [
            ['🂠', ' ', ' '],
            ['🂠', '🂠', '🂠'],
        ],
    ]

    def __init__(self, x, y, board, shape_index=None):
        self.x = x
        self.y = y
        self.board = board
        self.char = '🂠'
        # Randomly pick a shape if not provided
        shape_index = shape_index if shape_index is not None else random.randint(0, len(self.SHAPES) - 1)
        self.shape = shape_index
        self.layout = self.transpose_shape(self.SHAPES[shape_index])

    def move_left(self):
        if self.board.is_valid_move(self, self.x - 1, self.y):
            self.x -= 1

    def move_right(self):
        if self.board.is_valid_move(self, self.x + 1, self.y):
            self.x += 1

    def move_down(self):
        if self.board.is_valid_move(self, self.x, self.y + 1):
            self.y += 1

    def transpose_shape(self, shape):
        """Returns the transposed shape (swaps rows with columns)."""
        return [list(row) for row in zip(*shape)]
    
    def rotate_clockwise(self):
        # First, we transpose (if it's a valid move) the piece's layout by unpacking each row and zipping them together.
        # This flips the layout over its main diagonal (i.e., the diagonal that runs from the top-left to bottom-right).
        # Then, for each row in the transposed layout, we reverse the order of its cells using [::-1].
        # This results in a clockwise rotation of the layout.
        new_layout = [list(x)[::-1] for x in zip(*self.layout)]
        if self.board.is_valid_move(self, self.x, self.y, new_layout):
            self.layout = new_layout

    def rotate_counterclockwise(self):
        # To rotate counterclockwise, we first reverse the order of the rows in the layout using [::-1].
        # This flips the layout vertically (i.e., the top row becomes the bottom row and vice versa).
        # Then, we transpose the flipped layout by unpacking each row and zipping them together.
        # This results in a counterclockwise rotation of the layout.
        new_layout = [list(x) for x in zip(*self.layout[::-1])]
        if self.board.is_valid_move(self, self.x, self.y, new_layout):
            self.layout = new_layout
