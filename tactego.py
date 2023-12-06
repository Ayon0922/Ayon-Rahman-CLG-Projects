'''Filename: tactego.py
Author: Ayon Rahman
Date: 11/14/23
Section: 51
E-mail: ayonr1@umbc.edu
Description: A Python program to simulate a game of Tactego, a simplified version of Stratego.
The game involves two players with Red and Blue pieces,
 aiming to capture the enemy's flag or all enemy pieces on a 2D grid board.'''
import random

# Define constants for piece types and their strengths
FLAG = 'F'
ASSASSIN = 'A'
MINE = 'M'
SAPPER = 'S'


# Define a function to initialize the game board
def initialize_board(length, width):
    # Create an empty game board as a 2D list
    board = [[' ' for _ in range(width)] for _ in range(length)]
    return board


# Define a function to load pieces from a file
def load_pieces_from_file(filename):
    # Implement code to read the pieces from the file and create a list of pieces
    # Each piece should have a type (FLAG, ASSASSIN, MINE, SAPPER, or a number for strength)
    # and a count indicating how many of that piece type there are.
    pieces = []

    # Read the file and populate the pieces list
    file = open(filename, 'r')
    raw_data = file.readlines()
    for i in raw_data:
        l = i.replace('\n','').split(" ")
        for x in range(int(l[1])):
            pieces.append(l[0])

    return pieces


# Define a function to place pieces randomly on the board
def place_pieces_on_board(board, pieces, player):
    random.shuffle(pieces)
    pieces_left = len(pieces)
    if player == "Red":
        for r in range(len(board)):
            for c in range(len(board[r])):
                if pieces_left:
                    board[r][c] = "R" + pieces[len(pieces)- pieces_left]
                    pieces_left -= 1
    else:
        for r in range(len(board), 0, -1):
            for c in range(len(board[r-1])):
                if pieces_left:
                    board[r-1][c] = "B" + pieces[len(pieces)- pieces_left]
                    pieces_left -= 1



    # Implement code to place pieces on the board according to the rules you provided


# Define a function to display the current state of the board
def display_board(board):
    # Implement code to print the board with appropriate formatting
    row_size = len(board)
    column_size = len(board[0])
    lines = []
    for i in range(len(board)):
        line = "  "
        for j in range(len(board[i])):
            if board[i][j] != " ":
                line += board[i][j] + '  '
            else:
                line += "    "
        lines.append(line)

    for r in range(row_size +1):
        if r == 0:
            header = '   0'
            for i in range(column_size -1):
                header += '   ' + str(i+1)
            print(header)
        else:
            print(str(r-1) + lines[r-1])

def is_starting_position_valid(board,player,start_position):
    # what makes the starting position invalid
    # not in the range of length and width
    # if not red piece player
    # if the position does not have any piece
    x = int(start_position[0])
    y = int(start_position[1])
    is_valid = True
    if player == "Red":
        if (board[x][y][0] != 'R'):
            is_valid = False
        if (board[x][y] == ' ') or (board[x][y][1] == 'F'):
            is_valid = False
            print("You must select a starting position with one of your pieces, not a flag.")
    else:
        if (board[x][y][0] != 'B') or (board[x][y] == ' '):
            is_valid = False
        if (board[x][y] == ' ') or (board[x][y][1] == 'F'):
            is_valid = False
            print("You must select a starting position with one of your pieces, not a flag.")

    return is_valid




def is_ending_position_valid(board, player, ending_position, starting_position):
    # Not own pieces
    # has to be next position from the piece
    x = int(ending_position[0])
    y = int(ending_position[1])
    x_1 = int(starting_position[0])
    y_1 =  int(starting_position[1])
    is_valid = True
    if player == "Blue":
        if board[x][y][0] == 'B':
            is_valid = False
        if abs(x_1 - x) > 1 or abs(y_1 - y) > 1:
            is_valid = False
    else:
        if board[x][y][0] == 'R':
            is_valid = False
        if abs(x_1 - x) > 1 or abs(y_1 - y) > 1:
            is_valid = False

    return is_valid

# Define a function to check if a move is valid
def is_valid_move(board, player, start_position, end_position):
    is_valid = False
    if end_position == None:
        is_valid = is_starting_position_valid(board,player, start_position)
    else:
        is_valid = is_ending_position_valid(board, player, end_position, start_position)

    return is_valid



    # Implement code to check if the move is valid according to the game rules


# Define a function to resolve combat between two pieces
def resolve_combat(attacker, defender):
    # Assassin rules
    if attacker[1] == ASSASSIN:
        return attacker if defender[1] != ASSASSIN else defender
    elif defender[1] == ASSASSIN:
        return defender

    # Mine and Sapper rules
    if attacker[1] == SAPPER and defender[1] == MINE:
        return attacker
    elif defender[1] == MINE:
        return ' '  # Mine is removed after defeating the attacker

    # Regular strength-based combat
    if attacker[1] != 'F' and defender[1] != 'F':
        return attacker if int(attacker[1]) >= int(defender[1]) else defender
    else:
        return attacker


def check_victory(board):
    red_flag_count = 0
    blue_flag_count = 0
    game_over = False
    for i in board:
        for j in i:
            if j == 'RF':
                red_flag_count += 1
            elif j == 'BF':
                blue_flag_count += 1
    if red_flag_count == 0:
        print("Blue wins!")
        game_over = True
        display_board(board)
    elif blue_flag_count == 0:
        print("Red wins!")
        game_over = True
        display_board(board)

    return game_over

# Define a function to play the main game loop
def play_game(filename, length, width):
    # Initialize the game board
    board = initialize_board(length, width)

    # Load pieces from the file
    pieces = load_pieces_from_file(filename)

    # Randomly place pieces for both players
    place_pieces_on_board(board, pieces, 'Red')
    place_pieces_on_board(board, pieces, 'Blue')

    # display_board(board)

    # Initialize other game-related variables, e.g., player's turn, victory condition
    game_over =  False
    player_red_turn = True
    # Enter the main game loop
    while not game_over:

        # Display the current state of the board
        display_board(board)
        if player_red_turn:
            print("\nR Player's Turn: ")
        else:
            print("\nB Player's Turn: ")
        # Get the player's move (start_position and end_position)
        start_input = None
        end_input = None

        # Check if the move is valid
        running = True
        # Move the piece on the board
        while running:
            start_input = input("Select Piece to Move by Position >> ").split(" ")
            if ((player_red_turn and is_valid_move(board, 'Red', start_input,end_input)) or
                    (not player_red_turn and is_valid_move(board, "Blue", start_input, end_input))):

                break

        while running:
            end_input = input("Select Position to move Piece >> ").split(" ")
            if ((player_red_turn and is_valid_move(board, 'Red', start_input,end_input)) or
                    (not player_red_turn and is_valid_move(board, "Blue", start_input, end_input))):

                break

        # Resolve combat if necessary

        # Check for victory condition


        # Switch the player's turn

        start_x = int(start_input[0])
        start_y = int(start_input[1])
        end_x = int(end_input[0])
        end_y = int(end_input[1])
        if board[end_x][end_y] != ' ':
            winner = resolve_combat(board[start_x][start_y], board[end_x][end_y])
        else:
            winner = board[start_x][start_y]

        board[end_x][end_y] = winner
        board[start_x][start_y] = " "

        game_over = check_victory(board)
        player_red_turn = not player_red_turn



# Define the main function to start the game
def tactego(pieces_file, length, width):
    play_game(pieces_file, length, width)


if __name__ == '__main__':
    random.seed(input('What is seed? '))
    file_name = input('What is the filename for the pieces? ')
    length = int(input('What is the length? '))
    width = int(input('What is the width? '))
    tactego(file_name, length, width)
