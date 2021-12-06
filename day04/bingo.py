import numpy as np

def read_numbers():
    file = open('numbers.txt', "r")
    f1 = file.read()
    file.close()

    str_numbers = f1.split(",")
    num = []
    for n in str_numbers: num.append(int(n))

    return num


def read_boards():
    file = open('boards.txt', "r")
    f2 = file.read()
    file.close()

    f3 = f2.split("\n\n")  # Gives array of unique bingo cards
    f4 = []
    for i in range(len(f3)):
        card_data = f3[i].split("\n")
        card_j = []
        for c in card_data:
            line_str = c.split(" ")
            line_int = []
            for l in line_str:
                try:
                    line_int.append(int(l))
                except ValueError:
                    print('int < 10')
            card_j.append(line_int)
        f4.append(card_j)

    print(f4)
    return f4


def number_drawn(board,current_board, number):
    # print('Number:',number)
    new_board = current_board.copy()
    for i in range(len(board)):
        # print(board[i])
        for j in range(len(board[i])):
            for k in range(len(board[i][j])):
                if board[i][j][k] == number:
                    new_board[i][j][k] = 1
                    # print('Cross on board',i)

    return new_board


# Count for every board horizontally and vertically, if this sums up to 5 (the width of a bingo board), then return the number of the board
def check_bingo(current_board):
    bingo_board = -1
    for i in range(len(current_board)):
        row_sum = np.sum(current_board[i],axis=1)
        col_sum = np.sum(current_board[i],axis=0)

        if len(current_board[i]) in row_sum: bingo_board = i
        if len(current_board[i]) in col_sum: bingo_board = i

    return bingo_board


def calc_score(board, current_board, last_number):
    current_board_inv = np.ones([len(current_board),len(current_board)]) - current_board
    np_board = np.array(board)
    score_board = current_board_inv*np_board
    score = np.sum(score_board)
    # print(score)
    return score*last_number


def check_bingo2(current_board,bingo_list):

    for i in range(len(current_board)):

        if i not in bingo_list:
            row_sum = np.sum(current_board[i], axis=1)
            col_sum = np.sum(current_board[i], axis=0)

            if len(current_board[i]) in row_sum:
                bingo_list.append(i)
            elif len(current_board[i]) in col_sum:
                bingo_list.append(i)
    # print('Number of bingo boards',len(bingo_list))
    return bingo_list


# General
numbers = read_numbers()
boards = read_boards()
board_marked = np.zeros([len(boards),len(boards[0]),len(boards[0][0])])

# PT 1
ind_number = 0
ind_bingo_board = check_bingo(board_marked)

while ind_bingo_board==-1:
    # print(ind_number,"Draw number: ",numbers[ind_number])
    board_marked = number_drawn(boards, board_marked, numbers[ind_number])
    ind_bingo_board = check_bingo(board_marked)
    ind_number+=1

print(calc_score(boards[ind_bingo_board],board_marked[ind_bingo_board],numbers[ind_number-1]))


# PT 2
bingo_boards = []
ind_number = 0

while len(bingo_boards)<len(boards):
    board_marked = number_drawn(boards, board_marked, numbers[ind_number])
    bingo_boards = check_bingo2(board_marked,bingo_boards)
    ind_number+=1

print(calc_score(boards[bingo_boards[-1]],board_marked[bingo_boards[-1]],numbers[ind_number-1]))