def board_to_string(board):
    new_board = ''
    for row_index in range(len(board)):
        for col_index in range(len(board[row_index])):
            if col_index == 0:
                new_board += ('|' + ' ' + board[row_index][col_index] + ' ' + '|')
            elif col_index == len(board[row_index]) - 1:
                new_board += (' ' + board[row_index][col_index] + ' ' +  '|' + '\n')
            else:
                new_board += (' ' + board[row_index][col_index] + ' ' + '|')
    return new_board

board = [ ["X", "O", "#"],
          ["X", "X", "X"],
          ["#", "#", "#"] ]

result = board_to_string(board)

print(result)