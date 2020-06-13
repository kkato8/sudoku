# Date: 06/10/20
# Author: Ken Kato
# Description: generate a 3x3 sudoku
import copy
import random

# generate a 3x3 sudoku
def generate3x3():
    sudoku = [[".", ".", ".", ".",".",".",".",".","."],[".", ".", ".", ".",".",".",".",".","."],[".", ".", ".", ".",".",".",".",".","."],[".", ".", ".", ".",".",".",".",".","."], \
        [".", ".", ".", ".",".",".",".",".","."],[".", ".", ".", ".",".",".",".",".","."],[".", ".", ".", ".",".",".",".",".","."],[".", ".", ".", ".",".",".",".",".","."], \
            [".", ".", ".", ".",".",".",".",".","."]]

    poss1 = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
    poss2 = [[0,3],[0,4],[0,5],[1,3],[1,4],[1,5],[2,3],[2,4],[2,5]]
    poss3 = [[0,6],[0,7],[0,8],[1,6],[1,7],[1,8],[2,6],[2,7],[2,8]]
    poss4 = [[3,0],[3,1],[3,2],[4,0],[4,1],[4,2],[5,0],[5,1],[5,2]]
    poss5 = [[3,3],[3,4],[3,5],[4,3],[4,4],[4,5],[5,3],[5,4],[5,5]]
    poss6 = [[3,6],[3,7],[3,8],[4,6],[4,7],[4,8],[5,6],[5,7],[5,8]]
    poss7 = [[6,0],[6,1],[6,2],[7,0],[7,1],[7,2],[8,0],[8,1],[8,2]]
    poss8 = [[6,3],[6,4],[6,5],[7,3],[7,4],[7,5],[8,3],[8,4],[8,5]]
    poss9 = [[6,6],[6,7],[6,8],[7,6],[7,7],[7,8],[8,6],[8,7],[8,8]]

    for num in range(1,10):
        # 0 0 0 | . . . | . . .
        # 0 0 0 | . . . | . . .
        # 0 0 0 | . . . | . . . 
        # ----------------------
        # . . . | . . . | . . .
        # . . . | . . . | . . .
        # . . . | . . . | . . . 
        # ----------------------
        # . . . | . . . | . . .
        # . . . | . . . | . . .
        # . . . | . . . | . . . 
        try:
            sudoku = set3x3(sudoku, poss1, num)
        except TypeError:
            break

        # . . . | 0 0 0 | . . .
        # . . . | 0 0 0 | . . .
        # . . . | 0 0 0 | . . . 
        # ----------------------
        # . . . | . . . | . . .
        # . . . | . . . | . . .
        # . . . | . . . | . . . 
        # ----------------------
        # . . . | . . . | . . .
        # . . . | . . . | . . .
        # . . . | . . . | . . . 
        try:
            sudoku = set3x3(sudoku, poss2, num)
        except TypeError:
            break

        # . . . | . . . | 0 0 0
        # . . . | . . . | 0 0 0
        # . . . | . . . | 0 0 0 
        # ----------------------
        # . . . | . . . | . . .
        # . . . | . . . | . . .
        # . . . | . . . | . . . 
        # ----------------------
        # . . . | . . . | . . .
        # . . . | . . . | . . .
        # . . . | . . . | . . . 
        try:
            sudoku = set3x3(sudoku, poss3, num)
        except TypeError:
            break

        # . . . | . . . | . . .
        # . . . | . . . | . . .
        # . . . | . . . | . . . 
        # ----------------------
        # 0 0 0 | . . . | . . .
        # 0 0 0 | . . . | . . .
        # 0 0 0 | . . . | . . . 
        # ----------------------
        # . . . | . . . | . . .
        # . . . | . . . | . . .
        # . . . | . . . | . . . 
        try:
            sudoku = set3x3(sudoku, poss4, num)
        except TypeError:
            break

        # . . . | . . . | . . .
        # . . . | . . . | . . .
        # . . . | . . . | . . . 
        # ----------------------
        # . . . | 0 0 0 | . . .
        # . . . | 0 0 0 | . . .
        # . . . | 0 0 0 | . . . 
        # ----------------------
        # . . . | . . . | . . .
        # . . . | . . . | . . .
        # . . . | . . . | . . . 
        try:
            sudoku = set3x3(sudoku, poss5, num)
        except TypeError:
            break

        # . . . | . . . | . . .
        # . . . | . . . | . . .
        # . . . | . . . | . . . 
        # ----------------------
        # . . . | . . . | 0 0 0
        # . . . | . . . | 0 0 0
        # . . . | . . . | 0 0 0 
        # ----------------------
        # . . . | . . . | . . .
        # . . . | . . . | . . .
        # . . . | . . . | . . . 
        try:
            sudoku = set3x3(sudoku, poss6, num)
        except TypeError:
            break

        # . . . | . . . | . . .
        # . . . | . . . | . . .
        # . . . | . . . | . . . 
        # ----------------------
        # . . . | . . . | . . .
        # . . . | . . . | . . .
        # . . . | . . . | . . . 
        # ----------------------
        # 0 0 0 | . . . | . . .
        # 0 0 0 | . . . | . . .
        # 0 0 0 | . . . | . . . 
        try:
            sudoku = set3x3(sudoku, poss7, num)
        except TypeError:
            break

        # . . . | . . . | . . .
        # . . . | . . . | . . .
        # . . . | . . . | . . . 
        # ----------------------
        # . . . | . . . | . . .
        # . . . | . . . | . . .
        # . . . | . . . | . . . 
        # ----------------------
        # . . . | 0 0 0 | . . .
        # . . . | 0 0 0 | . . .
        # . . . | 0 0 0 | . . . 
        try:
            sudoku = set3x3(sudoku, poss8, num)
        except TypeError:
            break

        # . . . | . . . | . . .
        # . . . | . . . | . . .
        # . . . | . . . | . . . 
        # ----------------------
        # . . . | . . . | . . .
        # . . . | . . . | . . .
        # . . . | . . . | . . . 
        # ----------------------
        # . . . | . . . | 0 0 0
        # . . . | . . . | 0 0 0
        # . . . | . . . | 0 0 0 
        try:
            sudoku = set3x3(sudoku, poss9, num)
        except TypeError:
            break
        
    if sudoku == None:
        print("allover again")
        generate3x3()
    else:
        print()
        print("      A problem                     The answer   ")
        masked = copy.deepcopy(sudoku)
        masked = mask3x3(masked)
        print(" ".join(masked[0][0:3]) + " | " +  " ".join(masked[0][3:6]) + " | " +  " ".join(masked[0][6:9]) + "          " + " ".join(sudoku[0][0:3]) + " | " +  " ".join(sudoku[0][3:6])+ " | " +  " ".join(sudoku[0][6:9]))
        print(" ".join(masked[1][0:3]) + " | " +  " ".join(masked[1][3:6]) + " | " +  " ".join(masked[1][6:9]) + "          " + " ".join(sudoku[1][0:3]) + " | " +  " ".join(sudoku[1][3:6])+ " | " +  " ".join(sudoku[1][6:9]))
        print(" ".join(masked[2][0:3]) + " | " +  " ".join(masked[2][3:6]) + " | " +  " ".join(masked[2][6:9]) + "          " + " ".join(sudoku[2][0:3]) + " | " +  " ".join(sudoku[2][3:6])+ " | " +  " ".join(sudoku[2][6:9]))
        print("----------------------" + "          " + "---------------------")
        print(" ".join(masked[3][0:3]) + " | " +  " ".join(masked[3][3:6]) + " | " +  " ".join(masked[3][6:9]) + "          " + " ".join(sudoku[3][0:3]) + " | " +  " ".join(sudoku[3][3:6])+ " | " +  " ".join(sudoku[3][6:9]))
        print(" ".join(masked[4][0:3]) + " | " +  " ".join(masked[4][3:6]) + " | " +  " ".join(masked[4][6:9]) + "          " + " ".join(sudoku[4][0:3]) + " | " +  " ".join(sudoku[4][3:6])+ " | " +  " ".join(sudoku[4][6:9]))
        print(" ".join(masked[5][0:3]) + " | " +  " ".join(masked[5][3:6]) + " | " +  " ".join(masked[5][6:9]) + "          " + " ".join(sudoku[5][0:3]) + " | " +  " ".join(sudoku[5][3:6])+ " | " +  " ".join(sudoku[5][6:9]))
        print("----------------------" + "          " + "---------------------")
        print(" ".join(masked[6][0:3]) + " | " +  " ".join(masked[6][3:6]) + " | " +  " ".join(masked[6][6:9]) + "          " + " ".join(sudoku[6][0:3]) + " | " +  " ".join(sudoku[6][3:6])+ " | " +  " ".join(sudoku[6][6:9]))
        print(" ".join(masked[7][0:3]) + " | " +  " ".join(masked[7][3:6]) + " | " +  " ".join(masked[7][6:9]) + "          " + " ".join(sudoku[7][0:3]) + " | " +  " ".join(sudoku[7][3:6])+ " | " +  " ".join(sudoku[7][6:9]))
        print(" ".join(masked[8][0:3]) + " | " +  " ".join(masked[8][3:6]) + " | " +  " ".join(masked[8][6:9]) + "          " + " ".join(sudoku[8][0:3]) + " | " +  " ".join(sudoku[8][3:6])+ " | " +  " ".join(sudoku[8][6:9]))
        print()

# set a number at the designated position 
def set3x3(sudoku, poss, num):
    random.shuffle(poss)
    i = 0
    pos1 = poss[i][0]
    pos2 = poss[i][1]
    #print("pos1: {} pos2: {} num {}".format(pos1,pos2,num))
    while check3x3(sudoku, pos1, pos2, num) :
        try : 
            i += 1
            pos1 = poss[i][0]
            pos2 = poss[i][1]
            #print("pos1: {} pos2: {} num {}".format(pos1,pos2,num))
        except IndexError:
            break
    if i < len(poss):
        del poss[i]
        sudoku[pos1][pos2] = str(num)
        return sudoku
    else:
        return None

# checks if the number is filled correctly
def check3x3(sudoku, pos1, pos2, num):
    num = str(num)
    column = [column[pos2] for column in sudoku]
    row = sudoku[pos1]
    if pos1 == 0 or pos1 == 1 or pos1 == 2:
        if pos2 == 0 or pos2 == 1 or pos2 == 2:
            ele1 = sudoku[0][0]
            ele2 = sudoku[0][1]
            ele3 = sudoku[0][2]
            ele4 = sudoku[1][0]
            ele5 = sudoku[1][1]
            ele6 = sudoku[1][2]
            ele7 = sudoku[2][0]
            ele8 = sudoku[2][1]
            ele9 = sudoku[2][2]
            block = [ele1, ele2, ele3, ele4, ele5, ele6, ele7, ele8, ele9]
        elif pos2 == 3 or pos2 == 4 or pos2 == 5:
            ele1 = sudoku[0][3]
            ele2 = sudoku[0][4]
            ele3 = sudoku[0][5]
            ele4 = sudoku[1][3]
            ele5 = sudoku[1][4]
            ele6 = sudoku[1][5]
            ele7 = sudoku[2][3]
            ele8 = sudoku[2][4]
            ele9 = sudoku[2][5]
            block = [ele1, ele2, ele3, ele4, ele5, ele6, ele7, ele8, ele9]
        elif pos2 == 6 or pos2 == 7 or pos2 == 8:
            ele1 = sudoku[0][6]
            ele2 = sudoku[0][7]
            ele3 = sudoku[0][8]
            ele4 = sudoku[1][6]
            ele5 = sudoku[1][7]
            ele6 = sudoku[1][8]
            ele7 = sudoku[2][6]
            ele8 = sudoku[2][7]
            ele9 = sudoku[2][8]
            block = [ele1, ele2, ele3, ele4, ele5, ele6, ele7, ele8, ele9]
    elif pos1 == 3 or pos1 == 4 or pos1 == 5:
        if pos2 == 0 or pos2 == 1 or pos2 == 2:
            ele1 = sudoku[3][0]
            ele2 = sudoku[3][1]
            ele3 = sudoku[3][2]
            ele4 = sudoku[4][0]
            ele5 = sudoku[4][1]
            ele6 = sudoku[4][2]
            ele7 = sudoku[5][0]
            ele8 = sudoku[5][1]
            ele9 = sudoku[5][2]
            block = [ele1, ele2, ele3, ele4, ele5, ele6, ele7, ele8, ele9]
        elif pos2 == 3 or pos2 == 4 or pos2 == 5:
            ele1 = sudoku[3][3]
            ele2 = sudoku[3][4]
            ele3 = sudoku[3][5]
            ele4 = sudoku[4][3]
            ele5 = sudoku[4][4]
            ele6 = sudoku[4][5]
            ele7 = sudoku[5][3]
            ele8 = sudoku[5][4]
            ele9 = sudoku[5][5]
            block = [ele1, ele2, ele3, ele4, ele5, ele6, ele7, ele8, ele9]
        elif pos2 == 6 or pos2 == 7 or pos2 == 8:
            ele1 = sudoku[3][6]
            ele2 = sudoku[3][7]
            ele3 = sudoku[3][8]
            ele4 = sudoku[4][6]
            ele5 = sudoku[4][7]
            ele6 = sudoku[4][8]
            ele7 = sudoku[5][6]
            ele8 = sudoku[5][7]
            ele9 = sudoku[5][8]
            block = [ele1, ele2, ele3, ele4, ele5, ele6, ele7, ele8, ele9]
    elif pos1 == 6 or pos1 == 7 or pos1 == 8:
        if pos2 == 0 or pos2 == 1 or pos2 == 2:
            ele1 = sudoku[6][0]
            ele2 = sudoku[6][1]
            ele3 = sudoku[6][2]
            ele4 = sudoku[7][0]
            ele5 = sudoku[7][1]
            ele6 = sudoku[7][2]
            ele7 = sudoku[8][0]
            ele8 = sudoku[8][1]
            ele9 = sudoku[8][2]
            block = [ele1, ele2, ele3, ele4, ele5, ele6, ele7, ele8, ele9]
        elif pos2 == 3 or pos2 == 4 or pos2 == 5:
            ele1 = sudoku[6][3]
            ele2 = sudoku[6][4]
            ele3 = sudoku[6][5]
            ele4 = sudoku[7][3]
            ele5 = sudoku[7][4]
            ele6 = sudoku[7][5]
            ele7 = sudoku[8][3]
            ele8 = sudoku[8][4]
            ele9 = sudoku[8][5]
            block = [ele1, ele2, ele3, ele4, ele5, ele6, ele7, ele8, ele9]
        elif pos2 == 6 or pos2 == 7 or pos2 == 8:
            ele1 = sudoku[6][6]
            ele2 = sudoku[6][7]
            ele3 = sudoku[6][8]
            ele4 = sudoku[7][6]
            ele5 = sudoku[7][7]
            ele6 = sudoku[7][8]
            ele7 = sudoku[8][6]
            ele8 = sudoku[8][7]
            ele9 = sudoku[8][8]
            block = [ele1, ele2, ele3, ele4, ele5, ele6, ele7, ele8, ele9]
    if num in column or num in row or num in block:
        return True
    else:
        return False

def mask3x3(masked):
    for i in range(41):
        pos1 = random.randint(0,8)
        pos2 = random.randint(0,8)
        masked[pos1][pos2] = "."
    return masked

generate3x3()