# Tetris Game

This is a terminal-based implementation of the classic Tetris game. It is created using Python and the curses library for creating the game interface in the terminal.

## Prerequisites

- Python 3

## How to Run the Game

To play the game, run the `main.py` script from the command line:

```bash
python3 main.py 
```

## Game Controls

The controls for the game are as follows:

- `'a'`: Move the current piece to the left.
- `'l'`: Move the current piece to the right.
- `'q'`: Rotate the current piece counterclockwise.
- `'p'`: Rotate the current piece clockwise.
- `'Space'`: Drop the current piece to the bottom of the board.

## Game Description

In this Tetris game, pieces of different shapes fall from the top of the board. The objective of the game is to move and rotate the pieces so that they fill horizontal lines on the board. When a line is completely filled, it disappears and the player's score increases.

The game increases in speed every minute, making it more challenging as the game progresses. The game ends when a new piece cannot enter the game board because it is obstructed by other pieces.

The current score, high score, and the next piece to fall are displayed in the terminal window during gameplay. The high score is stored between games.

## File Structure

- `main.py`: The main script to run the game. It initializes the game and contains the main game loop.
- `board.py`: Defines the Board class. The board is the game area where the pieces fall. It handles the creation of the game board, rendering the board, merging pieces into the board, and checking for collisions.
- `pieces.py`: Defines the Piece class. A piece is an object that falls from the top of the board. It handles the shapes of the pieces, and the movement and rotation of the pieces.
- `game_state.py`: Defines the GameState class. It handles the current state of the game, including the current and next pieces, the score, and the high score.

## Author

Krzysztof Chylinski

## License

This project is licensed under the MIT License.
