from IPython.display import clear_output
import random


def printboard(board):
    clear_output(wait=True)
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])


def start():
    print("Welcome to Tic Tac Toe")


def player_input():
    marker = ''
    while marker not in ['X', 'O']:
        marker = input("Player 1: Choose your marker X or O: ").upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def place_marker(board, marker, position):
    board[position] = marker


def wincheck(board, marker):
    return ((board[1] == board[2] == board[3] == marker) or
            (board[4] == board[5] == board[6] == marker) or
            (board[7] == board[8] == board[9] == marker) or
            (board[1] == board[4] == board[7] == marker) or
            (board[2] == board[5] == board[8] == marker) or
            (board[3] == board[6] == board[9] == marker) or
            (board[1] == board[5] == board[9] == marker) or
            (board[3] == board[5] == board[7] == marker))


def choosefirst():
    if random.randint(1, 2) == 1:
        return "Player 1"
    else:
        return "Player 2"


def spacecheck(board, position):
    return board[position] == " "


def fullboard(board):
    for i in range(1, 10):
        if spacecheck(board, i):
            return False
    return True


def playerchoice(board):
    position = 0
    while position not in range(1, 10) or not spacecheck(board, position):
        position = int(input("Choose your next position (1-9): "))
    return position


def replay():
    choice = input("Do you want to play again? Enter Yes or No: ").lower()
    return choice == 'yes'


while True:
    board = [' '] * 10
    start()
    player1_marker, player2_marker = player_input()
    turn = choosefirst()
    print(turn + " will go first.")

    play_game = input('Are you ready to play? Enter Yes or No: ').lower()
    if play_game != 'yes':
        break

    game_on = True

    while game_on:
        if turn == "Player 1":
            printboard(board)
            position = playerchoice(board)
            place_marker(board, player1_marker, position)

            if wincheck(board, player1_marker):
                printboard(board)
                print("Congratulations! Player 1 has won the game!")
                game_on = False
            else:
                if fullboard(board):
                    printboard(board)
                    print("The game is a draw!")
                    break
                else:
                    turn = "Player 2"

        else:
            printboard(board)
            position = playerchoice(board)
            place_marker(board, player2_marker, position)

            if wincheck(board, player2_marker):
                printboard(board)
                print("Congratulations! Player 2 has won the game!")
                game_on = False
            else:
                if fullboard(board):
                    printboard(board)
                    print("The game is a draw!")
                    break
                else:
                    turn = "Player 1"

    if not replay():
        break

    #player 1 plays the game



    #player2 plays the game
