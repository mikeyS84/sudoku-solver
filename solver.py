import numpy as np

def sudoku_solver(sudoku):
    validSet = set()
    isValidSudoku = valid_starting_sudoku(sudoku, validSet)

    if not isValidSudoku:
        unsolvable(sudoku)
        return sudoku

    solveSudokuRecurse(sudoku, validSet)
    return sudoku

def solveSudokuRecurse(sudoku, validSet, x_prev=0, y_prev=0, recDepth=0):
    takenNumbersSet = set()
    x, y = get_next_zero(sudoku, x_prev, y_prev)

    if x == -1:
        return (sudoku, True)

    if sudoku[0][0] == -1:
        return False

    add_existing_numbers_to_set(x, y, takenNumbersSet, sudoku)

    for i in range(1,10):
        if i not in takenNumbersSet:
            sudoku[y][x] = i
            solved = solveSudokuRecurse(sudoku, validSet, x, y, recDepth + 1)
            takenNumbersSet.add(i)
            if solved:
                return True

    if recDepth == 0:
        unsolvable(sudoku)
        return sudoku

    sudoku[y][x] = 0
    return False

def valid_starting_sudoku(sudoku, validSet):
    for y in range(9):
        for x in range(9):
            if not check_valid(x, y, sudoku, validSet):
                return False
    return True

def get_next_zero(sudoku, x_prev, y_prev):
    for y in range(y_prev, 9):
        for x in range(x_prev, 9):
            if sudoku[y][x] == 0:
                return (x, y)
        x_prev = 0
    return (-1, -1)

def check_valid(x, y, sudoku, validSet):
    return check_valid_row(x, y, sudoku, validSet) and check_valid_column(x, y, sudoku, validSet) and check_valid_square(x, y, sudoku, validSet)

def check_valid_row(x, y, sudoku, validSet):
    for i in range(9):
        if not sudoku[y][i]:
            continue
        elif sudoku[y][i] not in validSet:
            validSet.add(sudoku[y][i])
        else:
            return False
    validSet.clear()
    return True 

def check_valid_column(x, y, sudoku, validSet):
    for i in range(9):
        if not sudoku[i][x]:
            continue
        elif sudoku[i][x] not in validSet:
            validSet.add(sudoku[i][x])
        else:
            return False
    validSet.clear()
    return True 

def check_valid_square(x, y, sudoku, validSet):
    x_offset = x//3 
    y_offset = y//3
    for i in range(3):
        for j in range(3):
            x2 = x_offset * 3 + j
            y2 = y_offset * 3 + i
            if not sudoku[y2][x2]:
                continue
            elif sudoku[y2][x2] not in validSet:
                validSet.add(sudoku[y2][x2])
            else:
                return False
    validSet.clear()
    return True  

def add_existing_numbers_to_set(x, y, sudSet, sudoku):
    add_row_to_set(y, sudSet, sudoku)
    add_column_to_set(x, sudSet, sudoku)
    add_square_to_set(x, y, sudSet, sudoku)
    
def add_row_to_set(y, sudSet, sudoku):
    sudSet.update(sudoku[y])

def add_column_to_set(x, sudSet, sudoku):
    for i in range(9):
        sudSet.add(sudoku[i][x])

def add_square_to_set(x, y, sudSet, sudoku):
    x_offset = x//3
    y_offset = y//3
    for i in range(3):
        for j in range(3):
            sudSet.add(sudoku[y_offset * 3 + i][x_offset * 3 + j])

def unsolvable(sudoku):
    for i in range(9):
        for j in range(9):
            sudoku[i][j] = -1
