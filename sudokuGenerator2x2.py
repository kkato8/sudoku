# Date: 06/13/20
# Author: Ken Kato
# Description: generate a 2x2 sudoku
import copy
import random

# generate a 2x2 sudoku
def generate2x2():
    sudoku = [[".", ".", ".", "."], [".", "." ,".", "."], [".", ".", ".", "."], [".", ".", ".", "."]]
    block1 = [[0,0],[0,1],[1,0],[1,1]]
    block2 = [[0,2],[0,3],[1,2],[1,3]]
    block3 = [[2,0],[2,1],[3,0],[3,1]]
    block4 = [[2,2],[2,3],[3,2],[3,3]]
    
    # place a number in each block in ascending order (1,2,3,4)
    for num in range(1,5):
        # 0 0 | . .
        # 0 0 | . .
        # ---------
        # . . | . .
        # . . | . .
        try:
            sudoku = set2x2(sudoku, block1, num)
        except TypeError:
            break

        # . , | 0 0
        # . . | 0 0
        # ---------
        # . . | . .
        # . . | . .
        try:
            sudoku = set2x2(sudoku, block2, num)
        except TypeError:
            break

        # . . | . .
        # . . | . .
        # ---------
        # 0 0 | . .
        # 0 0 | . .
        try:
            sudoku = set2x2(sudoku, block3, num)
        except TypeError:
            break

        # . . | . .
        # . . | . .
        # ---------
        # . . | 0 0
        # . . | 0 0
        try:
            sudoku = set2x2(sudoku, block4, num)
        except TypeError:
            break

    # if it failes to generate a sudoku, regenerate it
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

# set a number in the designated block
def set2x2(sudoku, block, num):
    random.shuffle(block)
    i = 0
    pos1 = block[i][0]
    pos2 = block[i][1]
    #print("pos1: {} pos2: {} num {}".format(pos1,pos2,num))
    while check2x2(sudoku, pos1, pos2, num) : # while the number is filled incorrectly
        try : 
            i += 1
            pos1 = poss[i][0] # change the position
            pos2 = poss[i][1] # change the position
            #print("pos1: {} pos2: {} num {}".format(pos1,pos2,num))
        except IndexError:
            break
    if i < len(block):
        del block[i] # delete the position
        sudoku[pos1][pos2] = str(num) # update a sudoku
        return sudoku
    else:
        return None

# checks if the number is filled correctly
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
    
# mask the number randomly
def mask2x2(masked):
    for i in range(8):
        pos1 = random.randint(0,3)
        pos2 = random.randint(0,3)
        masked[pos1][pos2] = "."
    return masked

generate2x2()
