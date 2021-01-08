def validate_sudoku():

    def check_vertical(digit,col_num):
        col_digits = []
        for row_num in range(9):
            col_digits.append(board[row_num][col_num])
        if col_digits.count(digit) > 1:
            return -1
        return 0

    col_num = 0
    for inner_list in board:
        for digit in inner_list:
            if digit.isnumeric() == True:
                if inner_list.count(digit) > 1:
                    return "false"
                else:
                    if check_vertical(digit,col_num) == -1:
                        return "false"
        col_num += 1
    return "true"

#provide matrix here.
board = [["5","3",".",".","7",".",".",".","."],
         ["5",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         ["5",".",".",".","8",".",".","7","9"]]

print(validate_sudoku())