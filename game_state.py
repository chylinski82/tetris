import time
import os

from pieces import Piece
from board import Board

class GameState:
    HIGH_SCORE_FILE = 'high_score.txt'

    def __init__(self):
        self.board = Board(20, 25)  # Create a new Board instance
        self.score = 0
        self.current_piece = Piece(10, 0, self.board)  # Create a piece at the top center of the board
        self.next_piece = Piece(10, 0, self.board)  # Create the next piece
        # Initialize the game start time
        self.start_time = time.time()
        self.high_score = self.load_high_score()

    def update_score(self, cleared_lines):
        """Update the score based on the number of lines cleared."""
        # clearing one line gives 100 points, clearing two lines gives 300 points, and so on.
        self.score += (cleared_lines ** 2) * 100
        #  updating potential new hi score
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score(self.high_score)

    def generate_next_piece(self):
        """Generate the next piece."""
        self.current_piece = self.next_piece
        self.next_piece = Piece(10, 0, self.board)
        return self.current_piece

    def get_current_piece(self):
        """Return the current piece."""
        return self.current_piece

    def get_score(self):
        """Return the current score."""
        return self.score

    def get_next_piece(self):
        """Return the next piece."""
        return self.next_piece
    
    def get_elapsed_time(self):
        """Return the elapsed time since the game started."""
        return time.time() - self.start_time
    
    def load_high_score(self):
        """Fetch hi score from text file, if no hi score is stored yet, fetch 0"""
        if os.path.isfile(self.HIGH_SCORE_FILE):
            with open(self.HIGH_SCORE_FILE, 'r') as file:
                return int(file.read())
        else:
            return 0

    def save_high_score(self, high_score):
        with open(self.HIGH_SCORE_FILE, 'w') as file:
            file.write(str(high_score))

