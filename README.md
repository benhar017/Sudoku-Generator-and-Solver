# Sudoku-Generator-and-Solver
### This project is mainly divided into two parts.
1. Sudoku Generation
2. Sudoku solving

The sudoku is generated accoring to the difficulty level given by the user. Any sudoku can be solved only if there exists more than 17 clues i.e atleast 17 boxes in the grid have to be filled.
For this project I have selected 23 clues for hard, 30 for medium level and 35 clues for easy level.
The algorithm used for solving the sudoku is backtracking
## Algorithm
1. Find the box which is empty.
2. Try placing each number from 1-9 in the box.
3. Check if the current digit is valid according to the rules of sudoku.
4. If valid Recursively perform steps 1-3.
5. Else, Empty the square and go back to the previous square.
6. Once we enter last square and it satisfies, we are done.

GUI library tkinter is used to make the interface for the sudoku grid and to provide solution. You can see the interface in the screenshots folder.
