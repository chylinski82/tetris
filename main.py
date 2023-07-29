import curses
import time

from game_state import GameState

# Define minimum required window size
MIN_WIN_HEIGHT = 35
MIN_WIN_WIDTH = 22

# Setup curses
stdscr = curses.initscr()
curses.curs_set(0)  # Makes the cursor invisible
stdscr.nodelay(True)  # Set to non-blocking mode

# Create a new GameState instance
game_state = GameState()

# Define the time interval for dropping the piece
drop_interval = 1.0
last_drop_time = time.time()

# Initialize the game start time
game_start_time = time.time()

# Initialize the time for speed increase
last_speed_increase_time = time.time()

try:
    while True:  # Main game loop
        # Get current window size
        height, width = stdscr.getmaxyx()

        # If the window size is too small, display a message and continue to next iteration
        if height < MIN_WIN_HEIGHT or width < MIN_WIN_WIDTH:
            stdscr.clear()
            stdscr.addstr(0, 0, "Window size is too small for the game. Press Ctrl + C and resize.")
            stdscr.refresh()
            time.sleep(0.1)
            continue

        # Get the current time in seconds
        current_time = time.time()

        # Calculate elapsed time
        elapsed_time = current_time - game_start_time

        # Increase the speed of the falling piece after every minute
        if current_time - last_speed_increase_time >= 60 and drop_interval > 0.2:
            drop_interval -= 0.05
            last_speed_increase_time = current_time  # Update the last speed increase time

        # Handle user inputs
        key = stdscr.getch()

        # Clear the old position of the piece
        game_state.board.merge_piece(game_state.get_current_piece(), is_clear=True)

        # Check if a key was pressed
        if key != -1:
            # Check which key was pressed and perform the corresponding action
            if key == ord('a'):
                game_state.get_current_piece().move_left()
            elif key == ord('l'):
                game_state.get_current_piece().move_right()
            elif key == ord('q'):
                game_state.get_current_piece().rotate_counterclockwise()
            elif key == ord('p'):
                game_state.get_current_piece().rotate_clockwise()
            elif key == ord(' '):
                # If the spacebar is pressed, move the piece down until it hits the bottom
                while not game_state.board.collide(game_state.get_current_piece()):
                    game_state.get_current_piece().move_down()

        # If it's time to move the piece down, do so
        if current_time - last_drop_time > drop_interval:
            if not game_state.board.collide(game_state.get_current_piece()):
                game_state.get_current_piece().move_down()
            else:
                # The piece has collided, so generate a new one at the top center of the board
                game_state.board.merge_piece(game_state.get_current_piece())
                cleared_lines = game_state.board.clear_complete_lines()
                game_state.update_score(cleared_lines)
                game_state.generate_next_piece()

                # If the newly generated piece collides immediately, it's game over
                if game_state.board.collide(game_state.get_current_piece()):
                    break

            last_drop_time = current_time

        # Merge the new position of the piece with the board
        game_state.board.merge_piece(game_state.get_current_piece())

        # Clear the curses screen to prepare for the next frame
        stdscr.clear()

        # Print each row of the board to the curses screen
        for row in game_state.board.board:
            # Join all the cells in the row into a single string and add a newline at the end
            # Then, print this string to the curses screen
            stdscr.addstr(''.join(row) + '\n')

        # Display the score
        stdscr.addstr(f"Score: {game_state.get_score()}\n")
        stdscr.addstr(f"High Score: {game_state.high_score}\n")

        # Display the next piece
        stdscr.addstr("Next piece:\n")
        stdscr.addstr(f"Elapsed time: {int(game_state.get_elapsed_time())} seconds\n")
        for row in game_state.get_next_piece().layout:
            stdscr.addstr(''.join(row) + '\n')

        # Refresh the curses screen to show the latest frame
        stdscr.refresh()

        # Pause the program for a short time (0.1 seconds) to create a brief delay between frames
        time.sleep(0.05)
finally:
    stdscr.clear()
    
    if game_state.board.collide(game_state.get_current_piece()):
        stdscr.addstr("Game Over\n")
    
    stdscr.refresh()
    time.sleep(2)
    # When the game loop is finished (either naturally or due to an exception),
    # make sure to end the curses application to return the terminal to its normal state
    curses.endwin()
