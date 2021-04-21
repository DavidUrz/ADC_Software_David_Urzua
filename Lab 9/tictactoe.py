# Implementation of Two Player Tic-Tac-Toe game in Python.
# 3 Bugs in place

''' We will make the board using dictionary
    in which keys will be the location(i.e : top-left,mid-right,etc.)
    and initialliy it's values will be empty space and then after every move
    we will change the value according to player's choice of move. '''

the_board = {'7': ' ', '8': ' ', '9': ' ',
             '4': ' ', '5': ' ', '6': ' ',
             '1': ' ', '2': ' ', '3': ' '}

board_keys = []

for key in the_board:
    board_keys.append(key)

''' We will have to print the updated board after every move in the game and
    thus we will make a function in which we'll define the print_board function
    so that we can easily print the board everytime by calling this function. '''

def print_board(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])  # First change
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

# Now we'll write the main function which has all the gameplay functionality.
def game():

    turn = 'X'
    count = 0


    while True:  # Second Fix
        print_board(the_board)
        print("It's your turn," + turn + ".Move to which place?")

        move = input()

        if the_board[move] == ' ':
            the_board[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        # Now we will check if player X or O has won,for every move after 5 moves.
        if count >= 5:
            if the_board['7'] == the_board['8'] == the_board['9'] != ' ':  # across the top
                print_board(the_board)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif the_board['4'] == the_board['5'] == the_board['6'] != ' ':  # across the middle
                print_board(the_board)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif the_board['1'] == the_board['2'] == the_board['3'] != ' ':  # across the bottom
                print_board(the_board)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif the_board['1'] == the_board['4'] == the_board['7'] != ' ':  # down the left side
                print_board(the_board)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif the_board['2'] == the_board['5'] == the_board['7'] != ' ':  # down the middle
                print_board(the_board)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif the_board['3'] == the_board['6'] == the_board['9'] != ' ':  # down the right side
                print_board(the_board)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif the_board['7'] == the_board['5'] == the_board['3'] != ' ':  # diagonal
                print_board(the_board)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif the_board['1'] == the_board['5'] == the_board['9'] != ' ':  # diagonal
                print_board(the_board)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")
            break  # Third change to match while

        # Now we have to change the player after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'

    # Now we will ask if player wants to restart the game or not.
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "N":
        for key in board_keys:
            the_board[key] = " "

        game()


if __name__ == "__main__":
    game()
