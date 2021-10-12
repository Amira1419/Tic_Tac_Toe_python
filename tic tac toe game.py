import random

def spaces_with_numbers(elem):
    return '|   '+str(elem)+'  '
    
def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    spaces = '|'+(' '*7)
    for i in range(0,3):
        print('+-------'*3,end='+\n')
        for j in range(0,3):
            if (j == 1):
                print(spaces_with_numbers(board[i][j-1]),spaces_with_numbers(board[i][j]),spaces_with_numbers(board[i][j+1]),end=' |\n')
            else:
                print(spaces * 3,end='|\n')
    print('+-------'*3,end='+\n')

def number_into_position(number_position):
    switcher = {
        1 : (0,0),
        2 : (0,1),
        3 : (0,2),
        4 : (1,0),
        6 : (1,2),
        7 : (2,0),
        8 : (2,1),
        9 : (2,2)
    }
    return switcher.get(number_position)

def check_emptiness_of_position(number_position,board):

    i,j = number_into_position(number_position)
    return type(board[i][j]) is int
    

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    try:
        user_move = int(input("Enter your move: "))
        if user_move > 9 or user_move < 1:
            print("Numbers should be between 1 and 9 only")
            return None
        elif user_move == 5 or (not check_emptiness_of_position(user_move,board)):
            print("This position is not empty try another one")
            return None
        else:
            i,j = number_into_position(user_move)
            board[i][j] = 'O'
            display_board(board)
            return board
    except ValueError :
        print("Enter Number")
        return None
    

    


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_squares = []
    for i in range(1,10):
        if i == 5:continue
        if check_emptiness_of_position(i,board):
            free_squares.append(number_into_position(i))
    return free_squares        


def victory_for(board):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    winner = ''
    if(board[0][0] == board[0][1] and board[0][0] == board[0][2]):
        winner = board[0][0]
    elif(board[1][0] == board[1][1] and board[1][0] == board[1][2]):
        winner = board[1][0]
    elif(board[2][0] == board[2][1] and board[2][0] == board[2][2]):
        winner = board[2][0]
    elif(board[0][0] == board[1][0] and board[0][0] == board[2][0]):
        winner = board[0][0]
    elif(board[0][1] == board[1][1] and board[0][1] == board[2][1]):
        winner = board[0][1] 
    elif(board[0][2] == board[1][2] and board[0][2] == board[2][2]):
        winner = board[0][2]
    
    if(winner == '' and len(make_list_of_free_fields(board))== 0):
        print("Tie")
        return "Tie"
    elif(winner == 'X'):
        print("You Lost!")
        return "You Lost!"
    elif(winner == 'O'):
        print('You Won!')
        return 'You Won!'
    else: return None
        


def draw_move(board):
    # The function draws the computer's move and updates the board.
    found = False
    random_number = 0
    while not found:
        random_number = random.randrange(1,10)
        if(random_number != 5 and check_emptiness_of_position(random_number,board)):
            found = True
    i,j = number_into_position(random_number)
    board[i][j]='X'
    display_board(board)
    return board
            
        
    
    
board = [[1,2,3],[4,'X',6],[7,8,9]]    
display_board(board)
while(True):
    board_updated = enter_move(board)
    if (board_updated is not None):
        board = board_updated
        if(victory_for(board) is not None):
            break
        board = draw_move(board)
        if(victory_for(board) is not None):
            break
