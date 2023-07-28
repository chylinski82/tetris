import time

class Board:
    def __init__(self, width, height, border_char='▯', empty_char='·'):
        # The board width and height are set as per user requirements
        self.width = width
        self.height = height
        # The border_char will be used to represent the borders of the game
        self.border_char = border_char
        # The empty_char will represent the empty spaces in the game
        self.empty_char = empty_char
        # Create the initial game board and a copy of it
        self.board = self.create_board()
        self.initial_board = [row.copy() for row in self.board]

    def create_board(self):
        """Creates a new game board with empty cells and borders."""
        # The game board is represented as a list of lists, where each inner list is a row in the game
        # We add the border_char on the sides and the empty_char in between for each row
        # Finally, we add a row of border_char at the bottom only
        board = []
        for y in range(self.height):
            row = []
            for x in range(self.width + 2):
                if x == 0 or x == self.width + 1:
                    row.append(self.border_char)
                else:
                    self.empty_char = ' ' if x % 2 == 1 else '·'
                    row.append(self.empty_char)
            board.append(row)

        board.append([self.border_char]*(self.width + 2))  # add border only at the bottom
        return board

    def render(self):
        """Prints the current state of the game board to the terminal."""
        # To render the board, we iterate over each cell in the board and print its value
        # The end="" argument in the print function prevents it from printing a newline after each cell
        for row in self.board:
            for cell in row:
                print(cell, end="")
            print()  # Print a newline at the end of each row

    def merge_piece(self, piece, is_clear=False):
        # Determine what character to use when merging. If is_clear is True, use the empty character.
        # Otherwise, use the piece's character.
        for i, row in enumerate(piece.layout):
            for j, cell in enumerate(row):
                if cell == piece.char:
                    if is_clear:
                        # Revert to the initial state of the cell
                        self.board[piece.y + i][piece.x + j] = self.initial_board[piece.y + i][piece.x + j]
                    else:
                        self.board[piece.y + i][piece.x + j] = piece.char

    def is_valid_move(self, piece, new_x, new_y, new_layout=None):
        """Checks if the piece can move to a new position or rotate without colliding with other pieces or borders."""
        layout = new_layout if new_layout else piece.layout
        for i, row in enumerate(layout):
            for j, cell in enumerate(row):
                if cell == piece.char:
                    # Check for collision with the left and right walls
                    if new_x + j < 1 or new_x + j > self.width:
                        return False
                    # Check for collision with the floor
                    if new_y + i > self.height:
                        return False
                    # Check for collision with other pieces
                    if self.board[new_y + i][new_x + j] not in {self.empty_char, ' '}:
                        return False
        return True

    def collide(self, piece):
        """Checks if the piece collides with the floor or another piece below it."""
        return not self.is_valid_move(piece, piece.x, piece.y + 1)

    def clear_complete_lines(self):
        """Removes complete lines from the board and adds new lines on top."""
        # We start from the bottom of the board and go up
        y = len(self.board) - 2  # we subtract 2 to ignore the very last line which is always a border
        cleared_lines = 0
        while y > 0:  # we stop at the first line because it's a border
            # Check if all cells (except the borders) contain a piece
            if all(cell == '🂠' for cell in self.board[y][1:-1]):  # we ignore the first and last cell of each line because they are borders
                self.board.pop(y)
                self.board.insert(1, self.initial_board[1].copy())
                cleared_lines += 1
            else:
                y -= 1

        return cleared_lines  # Returns the number of cleared lines


