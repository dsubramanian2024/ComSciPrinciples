'''
Crystal Game Project
Author: Divya Subramanian
'''
from shapes import shape #box is the name of the class
import sys # to get command line arguements
import random

def randshape():
    # generates random shapes with a chess piece and its corresponding symbol
    symbolArr = ["♟", "♞", "♝", "♜", "♛", "♚"]
    valueArr = [1, 3, 3, 5, 9, 100]
    r = random.randint(0, len(symbolArr) - 1)
    return shape(symbolArr[r], valueArr[r])

def startboardfunc(n):
    # creates a board, size n by n, with question marks
    rows, cols = (n, n)
    board = [[shape("?") for i in range(cols)] for j in range(rows)]
    return board

def shapeboardfunc(n):
    # creates a board, size n by n, with the shape symbols
    rows, cols = (n, n)
    board = [[ randshape() for i in range(cols)] for j in range(rows)]
    return board

def printboard(board):
    # prints the board with borders
    print("----" * len(board) + "-")
    for r in range (len(board)):
        for c in range(len(board[r])):
            print("|", end = " ")
            print(board[r][c].name, end = " ")
        print("|" + "\n" + "----" * len(board) + "-")

def ctArr(arr, shape):
    # keeps count of the number of times each shape appeared in a row, column, or diagonal
    if (shape.name == '♟'):
        arr[0] += 1
    elif (shape.name == '♞'):
        arr[1] += 1
    elif (shape.name == '♝'):
        arr[2] += 1
    elif (shape.name == '♜'):
        arr[3] += 1
    elif (shape.name == '♛'):
        arr[4] += 1
    elif (shape.name == '♚'):
        arr[5] += 1

def calcSum(arr):
    # calculates the sum of the row, column, or diagonal
    valueArr = [1, 3, 3, 5, 9, 100]
    sum = 0
    for i in range(len(valueArr)):
        sum += (arr[i] * arr[i]) * valueArr[i] # if there are n number of the same shape in a chosen row, column, or diagonal, the values of each of those shapes will be n x the value of the shape
    return sum

def row_sum(board, row):
    # adds and returns the sum of the values in the chosen row
    arr = [0, 0, 0, 0, 0, 0]
    cols = len(board[0])
    sum = 0
    for i in range (cols):
        ctArr(arr, board[row][i])
    return calcSum(arr)

def col_sum(board, col):
    # adds and returns the sum of the values in the chosen row
    arr = [0, 0, 0, 0, 0, 0]
    sum = 0
    for i in range (len(board)):
        ctArr(arr, board[i][col])
    return calcSum(arr)

def diagonal_sum(board, bool):
    arr = [0, 0, 0, 0, 0, 0]
    # adds and returns the sum of the values in the chosen diagonal
    sum = 0
    if bool: # if bool is true, diagonal from top left to bottom right
        for i in range (len(board)):
            ctArr(arr, board[i][i])
    else: # other diagonal
        for i in range (len(board)):
            ctArr(arr, board[i][len(board) - i - 1])
    return calcSum(arr)

def wantSwitch(type, board, num, n, oldsum):
    # checks if the user wants to randomly switch out an element for another and calculates and returns the new sum
    switch = input("Would you like to switch out one of the elements in your chosen row, column or diagonal? If so enter 'yes', everything else will be considered a no: ")
    if (switch == 'yes'):
        if (type == 'c'):
            elem = int(input("Which element in your column would you like to be randomly switched? (it can be anything up until but not including the length of the board and 0 is the top, 1 is the next and so on): "))
            checkinp(elem, n)
            board[elem][num] = randshape()
            sum = col_sum(board, num)
        elif (type == 'd'):
            elem = int(input("Which element in your diagonal would you like to be randomly switched? (it can be anything up until but not including the length of the board and 0 is the left most, 1 is the next and so on): "))
            checkinp(elem, n)
            if (num == 0):
                board[elem][elem] = randshape()
            else: # when num == 1 (\)
                board[n - elem - 1][elem] = randshape()
            sum = diagonal_sum(board, num)
        else:
            elem = int(input("Which element in your row would you like to be randomly switched? (it can be anything up until but not including the length of the board and 0 is the left most, 1 is the next and so on): "))
            checkinp(elem, n)
            board[num][elem] = randshape()
            sum = row_sum(board, num)
        print("Your new score is: " + str(sum))
        return sum
    return oldsum

def checkinp(num, n):
    # checks if the inputs are valid
    while (int(num) >= int(n) or int(num) < 0):
        num = input("Your input was invalid. Please enter a valid input: ")
    return num

def GetNCalcInp(board, n):
    # gets the row, column, or diagonal number and calls funcs to calculate sum
    type = input("Would you like to chose a row (anything either than 'c' or 'd'), column (c), or diagonal (d): ")
    if (type == "c"):
        num = int(input("What column would you like to choose (it can be any integer from 0 up until but not including " + str(n) + "): "))
        num = checkinp(num, n)
        sum = col_sum(board, num)
    elif (type == "d"):
        num = int(input("What diagonal would you like to choose (it can be either 0 (/) or 1 (\\)): "))
        num = checkinp(num, 2)
        sum = diagonal_sum(board, num)
    else:
        num = int(input("What row would you like to choose (it can be any integer from 0 up until but not including " + str(n) + "): "))
        num = checkinp(num, n)
        sum = row_sum(board, num)
    print("Your score is: " + str(sum))
    printboard(board)
    newSum = wantSwitch(type, board, num, n, sum)
    return newSum

def calcWinner(sumArr):
    # finds and returns the element in the area with the most amount of points
    big = 0
    for i in range(len(sumArr)):
        if (sumArr[big] < sumArr[i]):
            big = i
    return big

def manyUsers(board2, n):
    # continues getting users, prints the board, calculates sums, and displays the winner
    inp = "yes"
    nameArr = []
    sumArr = []
    while (inp == "yes"): # continues getting new users until anything other than 'yes' is inputted
        nameArr.append(input("Enter a name: "))
        sum = GetNCalcInp(board2, n)
        sumArr.append(sum)
        inp = input("Would you like to have another user? If so enter 'yes', anything else will be considered a no: ")
    print("Here is the randomly generated board: ")
    printboard(board2) # displays the board
    print("Scores:")
    for i in range(len(sumArr)):
        print(nameArr[i] + ": " + str(sumArr[i])) # displays each users name and score
    big = calcWinner(sumArr)
    print("Congrats " + nameArr[big] + " has won with a subtotal of " + str(sumArr[big]) + " points! Yayyy!")

def main():
    n = int(input("Hi! Welcome to Divya's Crystal Game! Please enter a size of the board you would like: "))
    board1 = startboardfunc(n)
    printboard(board1) # prints the board with question marks
    board2 = shapeboardfunc(n)
    manyUsers(board2, n)

main()
