"""
File:    mancala.py
Author:  Ayon Rahman
Date:    11/03/23
Section: 51
E-mail:  ayonr1@umbc.edu
Description:
  its the commandline mancala game in python
	"""
BLOCK_WIDTH = 6
BLOCK_HEIGHT = 5
BLOCK_SEP = "*"
SPACE = ' '


def draw_board(top_cups, bottom_cups, mancala_a, mancala_b):
    """
    draw_board is the function that you should call in order to draw the board.
        top_cups and bottom_cups are lists of strings.  Each string should be length BLOCK_WIDTH and each list should be of length BLOCK_HEIGHT.
        mancala_a and mancala_b should be lists of strings.  Each string should be BLOCK_WIDTH in length, and each list should be 2 * BLOCK_HEIGHT + 1

    :param top_cups: This should be a list of strings that represents cups 1 to 6 (Each list should be at least BLOCK_HEIGHT in length, since each string in the list is a line.)
    :param bottom_cups: This should be a list of strings that represents cups 8 to 13 (Each list should be at least BLOCK_HEIGHT in length, since each string in the list is a line.)
    :param mancala_a: This should be a list of 2 * BLOCK_HEIGHT + 1 in length which represents the mancala at position 7.
    :param mancala_b: This should be a list of 2 * BLOCK_HEIGHT + 1 in length which represents the mancala at position 0.
    """
    board = [[SPACE for _ in range((BLOCK_WIDTH + 1) * (len(top_cups) + 2) + 1)] for _ in range(BLOCK_HEIGHT * 2 + 3)]
    for p in range(len(board)):
        board[p][0] = BLOCK_SEP
        board[p][len(board[0]) - 1] = BLOCK_SEP

    for q in range(len(board[0])):
        board[0][q] = BLOCK_SEP
        board[len(board) - 1][q] = BLOCK_SEP

    # draw midline
    for p in range(BLOCK_WIDTH + 1, (BLOCK_WIDTH + 1) * (len(top_cups) + 1) + 1):
        board[BLOCK_HEIGHT + 1][p] = BLOCK_SEP

    for i in range(len(top_cups)):
        for p in range(len(board)):
            board[p][(1 + i) * (1 + BLOCK_WIDTH)] = BLOCK_SEP

    for p in range(len(board)):
        board[p][1 + BLOCK_WIDTH] = BLOCK_SEP
        board[p][len(board[0]) - BLOCK_WIDTH - 2] = BLOCK_SEP

    for i in range(len(top_cups)):
        draw_block(board, i, 0, top_cups[i])
        draw_block(board, i, 1, bottom_cups[i])

    draw_mancala(0, mancala_a, board)
    draw_mancala(1, mancala_b, board)

    print('\n'.join([''.join(board[i]) for i in range(len(board))]))


def draw_mancala(fore_or_aft, mancala_data, the_board):
    """
        Draw_mancala is a helper function for the draw_board function.
    :param fore_or_aft: front or back (0, or 1)
    :param mancala_data: a list of strings of length 2 * BLOCK_HEIGHT + 1 each string of length BLOCK_WIDTH
    :param the_board: a 2d-list of characters which we are creating to print the board.
    """
    if fore_or_aft == 0:
        for i in range(len(mancala_data)):
            data = mancala_data[i][0: BLOCK_WIDTH].rjust(BLOCK_WIDTH)
            for j in range(len(mancala_data[0])):
                the_board[1 + i][1 + j] = data[j]
    else:
        for i in range(len(mancala_data)):
            data = mancala_data[i][0: BLOCK_WIDTH].rjust(BLOCK_WIDTH)
            for j in range(len(mancala_data[0])):
                the_board[1 + i][len(the_board[0]) - BLOCK_WIDTH - 1 + j] = data[j]


def draw_block(the_board, pos_x, pos_y, block_data):
    """
        Draw block is a helper function for the draw_board function.
    :param the_board: the board is the 2d grid of characters we're filling in
    :param pos_x: which cup it is
    :param pos_y: upper or lower
    :param block_data: the list of strings to put into the block.
    """
    for i in range(BLOCK_HEIGHT):
        data = block_data[i][0:BLOCK_WIDTH].rjust(BLOCK_WIDTH)
        for j in range(BLOCK_WIDTH):
            the_board[1 + pos_y * (BLOCK_HEIGHT + 1) + i][1 + (pos_x + 1) * (BLOCK_WIDTH + 1) + j] = data[j]


def get_player():
    player_1 = input("Player 1 please tell me your name: ")
    player_2 = input("Player 2 please tell me your name: ")
    return [player_1, player_2]


### CUSTOM FUNC TO PRINT THE BOARD
def print_board(cups, players):
    ## TOP ROWS
    top_rows = []
    for cup_idx in range(1, 7):
        current_cell = []

        current_cell.append('Cup'.ljust(BLOCK_WIDTH))
        current_cell.append(f'{cup_idx}'.rjust(BLOCK_WIDTH))
        current_cell.append('Stones'.ljust(BLOCK_WIDTH))
        current_cell.append(f'{cups[cup_idx]}'.rjust(BLOCK_WIDTH))
        current_cell.append(' ' * BLOCK_WIDTH)

        top_rows.append(current_cell)

    ## BOTTOM ROWS
    bottom_rows = []
    for cup_idx in range(13, 7, -1):
        current_cell = []

        current_cell.append('Cup'.ljust(BLOCK_WIDTH))
        current_cell.append(f'{cup_idx}'.rjust(BLOCK_WIDTH))
        current_cell.append('Stones'.ljust(BLOCK_WIDTH))
        current_cell.append(f'{cups[cup_idx]}'.rjust(BLOCK_WIDTH))
        current_cell.append(' ' * BLOCK_WIDTH)

        bottom_rows.append(current_cell)

    ## First mancala--> left side for player 2
    first_mancala = []
    for i in range(BLOCK_HEIGHT * 2 + 1):
        if i == 3:
            first_mancala.append(f'{players[1]}'.ljust(BLOCK_WIDTH))
        elif i == 7:
            first_mancala.append('Stones'.ljust(BLOCK_WIDTH))
        elif i == 8:
            first_mancala.append(f'{cups[0]}'.ljust(BLOCK_WIDTH))
        else:
            first_mancala.append(' ' * BLOCK_WIDTH)

    ### Second Mancala---> right side for player 1
    sec_mancala = []
    for i in range(BLOCK_HEIGHT * 2 + 1):
        if i == 3:
            sec_mancala.append(f'{players[0]}'.ljust(BLOCK_WIDTH))
        elif i == 7:
            sec_mancala.append('Stones'.ljust(BLOCK_WIDTH))
        elif i == 8:
            sec_mancala.append(f'{cups[7]}'.ljust(BLOCK_WIDTH))
        else:
            sec_mancala.append(' ' * BLOCK_WIDTH)

    draw_board(top_rows, bottom_rows, first_mancala, sec_mancala)


def take_turn(player, cups, player_names):
    # Game over flag that we return in the end.
    game_over = False

    ### RUNNING THE GAME ###
    while True:
        # Using my custom print function
        print_board(cups, player_names)

        # Checking player input validity--->
        while True:
            player_cup_selected = int(input(f'{player} What cup do you want to move? '))
            if -1 < player_cup_selected < 14 and (player_cup_selected != 0 or player_cup_selected != 7):
                break

        stones_selected = cups[player_cup_selected]
        next_cup = player_cup_selected + 1

        # remove all the stones from the cup selected
        cups[player_cup_selected] = 0

        # Iterate until stone_selected are all placed in the cups
        while stones_selected:
            if next_cup > 13:
                next_cup = 0

            cups[next_cup] += 1

            # we add one to go to the next cup
            next_cup += 1
            # we remove one stone from out hand as we placed in it in the cup
            stones_selected -= 1

        # Check if the last stone was placed in mancala cup i.e other than cup 0 or 7
        # we break this loop as this player has no longer turn
        if (next_cup - 1 != 0 and next_cup - 1 != 7):
            break

        print('Your last stone landed in a mancala.  \nGo again please...')

        # check if the game is over: we do this by calculating the sum of cups in each row
        # as, if the sum is zero then no bead is left in that row, thus the game is over.
        if sum(cups[1:7]) == 0 or sum(cups[8:14]) == 0:
            game_over = True
            break

    # returning values
    return game_over, cups


def run_game():
    player_names = get_player()
    game_over = False
    player_1_turn = True

    # cups is a 1d list where index 0 and 7 are the non-mancala cups, we'll use
    # condition to make sure the beads and inputs are valid.
    cups = []
    for i in range(14):
        if i != 0 and i != 7:
            cups.append(4)
        else:
            cups.append(0)

    while not game_over:
        if player_1_turn:
            game_over, cups = take_turn(player_names[0], cups, player_names)
        else:
            game_over, cups = take_turn(player_names[1], cups, player_names)

        # we alternate turns
        player_1_turn = not player_1_turn

    # After the game is over, finally print the board one more time and state the winner
    print_board(cups, player_names)
    if cups[0] > cups[7]:
        print(f'{player_names[1]} is the winner')
    elif cups[7] > cups[0]:
        print(f'{player_names[0]} is the winner')


if __name__ == "__main__":
    run_game()


