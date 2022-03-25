"""
Name: Brandon Trapp
lab9.py

I certify that this assignment is entirely my own work.

"""


def build_board():

    number_list = [1,2,3,4,5,6,7,8,9]
    return number_list

def print_board(board):
    """ prints the values of baord """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = []
    for v in board:
        new_board.append(v)
    for i in range(len(board)):
        if str(board[i]).find('x') >= 0:
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif str(board[i]).find('o') >= 0:
            new_board[i] = BLUE + board[i] + LIGHT_GRAY
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(new_board[0], new_board[1], new_board[2])
    row_2 = row_format.format(new_board[3], new_board[4], new_board[5])
    row_3 = row_format.format(new_board[6], new_board[7], new_board[8])
    row_separator = '-' * 11
    print(LIGHT_GRAY)
    print(row_1)
    print(row_separator)
    print(row_2)
    print(row_separator)
    print(row_3)
    print(reset)

def is_legal(board, position):

    if str(board[position-1]).isnumeric():
        return True
    else:
        return False

def fill_spot(board, position, character):
    character = character.strip()

    board[position - 1] = character.lower()

def winning_game(board):

    if board[0] == board[1] == board[2]:
        return True
    elif board[2]==board[4]==board[6]:
        return True
    elif board[6]==board[7]==board[8]:
        return True
    elif board[2]==board[5]==board[8]:
        return True
    elif board[0]==board[3]==board[6]:
        return True
    elif board[0]==board[4]==board[8]:
        return True
    else:
        return False

def game_over(board):

    game = winning_game(board)
    if game == True:
        return True
    else:
        return False

def get_winner(board):
    pass

def play(board):

   print("Enter a number on the board to put an x or o into the spot. ")
   play = "y" or "Y"
   while play == "y" or "Y":
       print_board(board)
       while game_over(board) == False:
           player1 = eval(input("Player x, pick a spot with a number: "))
           if is_legal(board, player1) == True:
               fill_spot(board,player1,'x')
           else:
               print("Pick again")

           player2 = eval(input("Player o, pick a spot with a number"))
           if is_legal(board, player2) == True:
               fill_spot(board, player2, "o")
           else:
               print("pick again")

def main():
    play(build_board())


if __name__ == '__main__':
    main()
