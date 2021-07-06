
import random

grid = [[0 for x in range(9)] for y in range(9)]

# To print the grid 
def print_grid(g):
    for i in range(len(g)):
        if i%3 == 0 and i != 0:
            print("---------------------")
        for j in range(len(g[0])):
                if j%3 == 0 and j != 0:
                    print("|",end="")
                if j == 8:
                    print(g[i][j])
                else:
                    print(str(g[i][j])+" ",end="")
# To return the row and col where the box is empty
def is_empty(g):
    for i in range(len(g)):
        for j in range(len(g[0])):
            if g[i][j] == 0:
                return(i,j) 
    return None            

def validate(g,number,position):
    # Traverse through row
    for i in range(len(g[0])):
        if g[position[0]][i] == number and position[1] != i:
            return False 

    # Traverse through col
    for i in range(len(g)):
        if g[i][position[1]] == number and position[0] != i:
            return False       

    # Check the mini grid 3x3
    minigrid_row = position[1] // 3
    minigrid_col = position[0] // 3
    for i in range(minigrid_col*3,minigrid_col*3 + 3):
        for j in range(minigrid_row*3,minigrid_row*3 + 3):
            if g[i][j] == number and (i,j) != position:
                return False

    return True     

              
def sudoku_solve(grid):
    find = is_empty(grid)
    if not find:
        return True
    else:
        row,col = find 

    for i in range(1,10):
        if validate(grid, i, (row,col)):
            grid[row][col] = i

            if sudoku_solve(grid):
                return True

            grid[row][col] = 0
    return False        




def MakeSudoku(n):
    
            
    for i in range(9):
        for j in range(9):
            grid[i][j] = 0
            
    # The range here is the amount
	# of numbers in the grid
    for i in range(n):
        #choose random numbers
        row = random.randrange(9)
        col = random.randrange(9)
        num = random.randrange(1,10)
        while(not validate(grid,num,(row,col)) or grid[row][col] != 0): #if taken or not valid reroll
            row = random.randrange(9)
            col = random.randrange(9)
            num = random.randrange(1,10)
        grid[row][col]= num;        



i=int(input("1.easy 2.difficult 3.hard   "))
if i == 1:
    MakeSudoku(35)
if i == 2:
    MakeSudoku(30)
if i == 3:
    MakeSudoku(23)        
print_grid(grid)
print()
sudoku_solve(grid)
print("####################")
print("Solution: ")
print_grid(grid)
