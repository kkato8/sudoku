# Date: 06/10/20
# Author: Ken Kato
# Description: generate a 2x2 sudoku
import copy
import random

# generate a 2x2 sudoku
def generate2x2():
    sudoku = [[".", ".", ".", "."], [".", "." ,".", "."], [".", ".", ".", "."], [".", ".", ".", "."]]

    # . . | . .
    # . . | . .
    # ---------
    # 0 0 | . .
    # 0 0 | . .
    poss = [[2, 0], [2, 1], [3, 0], [3, 1]]
    for i in range(4):
        pos1 = poss[i][0]
        pos2 = poss[i][1]
        sudoku = set2x2(sudoku, pos1, pos2)
    
    # 0 . | . .
    # 0 . | . .
    # ---------
    # . . | . .
    # . . | 0 0
    poss = [[0, 0], [1, 0], [3, 2], [3, 3]]
    for i in range(4):
        pos1 = poss[i][0]
        pos2 = poss[i][1]
        sudoku = set2x2(sudoku, pos1, pos2)
    

    # . 0 | . .
    # . 0 | . .
    # ---------
    # . . | 0 0
    # . . | . .
    poss = [[0, 1], [1, 1], [2, 2], [2, 3]]
    for i in range(4):
        pos1 = poss[i][0]
        pos2 = poss[i][1]
        sudoku = set2x2(sudoku, pos1, pos2)
    

    # . . | 0 0
    # . . | 0 0
    # ---------
    # . . | . .
    # . . | . .
    poss = [[0, 2], [0, 3], [1, 2], [1, 3]]
    for i in range(4):
        try :
            pos1 = poss[i][0]
            pos2 = poss[i][1]
            sudoku = set2x2(sudoku, pos1, pos2)
        except TypeError:
            break

    if sudoku == None:
        generate2x2()
    else:
        print()
        print("A problem          The answer")
        masked = copy.deepcopy(sudoku)
        masked = mask2x2(masked)
        print(" ".join(masked[0][0:2]) + " | " +  " ".join(masked[0][2:4]) + "          " + " ".join(sudoku[0][0:2]) + " | " +  " ".join(sudoku[0][2:4]))
        print(" ".join(masked[1][0:2]) + " | " +  " ".join(masked[1][2:4]) + "          " + " ".join(sudoku[1][0:2]) + " | " +  " ".join(sudoku[1][2:4]))
        print("---------" + "          " + "---------")
        print(" ".join(masked[2][0:2]) + " | " +  " ".join(masked[2][2:4]) + "          " + " ".join(sudoku[2][0:2]) + " | " +  " ".join(sudoku[2][2:4]))
        print(" ".join(masked[3][0:2]) + " | " +  " ".join(masked[3][2:4]) + "          " + " ".join(sudoku[3][0:2]) + " | " +  " ".join(sudoku[3][2:4]))
        print()

# set a number at the designated position 
def set2x2(sudoku, pos1, pos2):
    i = 0
    nums = [1,2,3,4]
    random.shuffle(nums)
    num = nums[i]
    while check2x2(sudoku, pos1, pos2, num) :
        try : 
            i += 1
            num = nums[i]
        except IndexError:
            break
    if i < 4: 
        sudoku[pos1][pos2] = str(num)
        return sudoku
    else:
        return None

# checks if the number is filled correctly (only for 2x2)
def check2x2(sudoku, pos1, pos2, num):
    num = str(num)
    column = [column[pos2] for column in sudoku]
    row = sudoku[pos1]
    if pos1 == 0 or pos1 == 1:
        if pos2 == 0 or pos2 == 1:
            ele1 = sudoku[0][0]
            ele2 = sudoku[0][1]
            ele3 = sudoku[1][0]
            ele4 = sudoku[1][1]
            block = [ele1, ele2, ele3, ele4]
        elif pos2 == 2 or pos2 == 3:
            ele1 = sudoku[0][2]
            ele2 = sudoku[0][3]
            ele3 = sudoku[1][2]
            ele4 = sudoku[1][3]
            block = [ele1, ele2, ele3, ele4]
    elif pos1 == 2 or pos1 == 3:
        if pos2 == 0 or pos2 == 1:
            ele1 = sudoku[2][0]
            ele2 = sudoku[2][1]
            ele3 = sudoku[3][0]
            ele4 = sudoku[3][1]
            block = [ele1, ele2, ele3, ele4]
        elif pos2 == 2 or pos2 == 3:
            ele1 = sudoku[2][2]
            ele2 = sudoku[2][3]
            ele3 = sudoku[3][2]
            ele4 = sudoku[3][3]
            block = [ele1, ele2, ele3, ele4]

    if num in column or num in row or num in block:
        return True
    else:
        return False

def mask2x2(masked):
    for i in range(8):
        pos1 = random.randint(0,3)
        pos2 = random.randint(0,3)
        masked[pos1][pos2] = "."
    return masked

generate2x2()