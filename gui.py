from tkinter import *
import random
import tkinter
import tkinter.messagebox
frame=Tk()
menu=Menu(frame)
file=Menu(menu)
file.add_command(label="Exit", command=frame.quit)
file.add_command(label="EASY LEVEL", command=lambda:easyLvl())
file.add_command(label="MEDIUM LEVEL", command=lambda:medLvl())
file.add_command(label="HARD LEVEL", command=lambda:hardLvl())


menu.add_cascade(label="Choose difficulty Level ", menu=file)
frame.config(menu=menu)



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

def is_empty(g):
    for i in range(len(g)):
        for j in range(len(g[0])):
            if g[i][j] == 0:
                return(i,j) 
    return None

def MakeSudoku(n):
    grid = [[0 for x in range(9)] for y in range(9)]        
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
    return grid    


def easyLvl():
    frame.title("easy level selected")
    n = 35
    grid = MakeSudoku(n) 
    createGrid(grid)

def medLvl():
    frame.title("medium level selected")
    n=30
    grid = MakeSudoku(n)
    createGrid(grid)

def hardLvl():
    frame.title("hard level selected")
    n = 23
    grid = MakeSudoku(n)
    createGrid(grid)

def sudoku_solve(g):
    find = is_empty(g)
    if not find:
        return True
    else:
        row,col = find 
    
    for i in range(1,10):
        if validate(g, i, (row,col)):
            g[row][col] = i
            if sudoku_solve(g):
                return True

            g[row][col] = 0
    return False
def sudoku(grid):
    sudoku_solve(grid)
    createGrid(grid)

def submission(grid):
    sudoku_solve(grid)
    g = grid.copy()
    sudoku_solve(g)
    if g == grid:
        tkinter.messagebox.showinfo("Result", "congratulations you made it!!")
    #else:
    tkinter.messagebox.showerror("Result ",  "Sorry incorrect ans!! Please try again")
    

colourTxt="black"
#-----------------------------MAIN CODE------------------
def createGrid(grid):
    for rowindex in range (9):
        for colindex in range (9):
            if (rowindex in (0,1,2,6,7,8) and colindex in (3,4,5) or \
                (rowindex in (3,4,5) and colindex in (0,1,2,6,7,8))):
                    colour="light blue"
            else:
                colour="white"

            x = grid[rowindex][colindex]

            if x==0:
                colourTxt="red"
                ent=Entry(frame,width=8, bg=colour,fg=colourTxt)
                ent.grid(row=rowindex, column=colindex, sticky=N+S+E+W)
            else:
                colourTxt="black" 
                btn = Label(frame, width=8, bg = colour,text=x, fg= colourTxt)
                btn.grid(row=rowindex, column=colindex,sticky=N+S+E+W)
                '''btn=Button(frame, width=8, bg=colour, text=x, fg=colourTxt)   
                btn.grid(row=rowindex, column=colindex, sticky=N+S+E+W)'''
            sub = Button(frame, width = 8, text = "Submit" ,bg = "yellow", command=lambda:submission(grid))  
            sub.grid(row= 9,column=0)
            sol = Button(frame, width=8, text = "See Solution", bg = "red", command=lambda:sudoku(grid))
            sol.grid(row=9, column=1) 



grid = [[0 for x in range(9)] for y in range(9)]                  
createGrid(grid)
frame.mainloop()