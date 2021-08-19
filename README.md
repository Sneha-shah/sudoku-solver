# sudoku-solver
GUI sudoku solver that combines manual and backtracking approaches for quicker solving. Uses python and tkinter.

![Screen Shot 2021-07-07 at 1 12 20 AM](https://user-images.githubusercontent.com/54175817/130054137-70c2ef4d-02db-4974-9158-51a3e7682de6.png)
![Screen Shot 2021-07-07 at 1 16 21 AM](https://user-images.githubusercontent.com/54175817/130054146-23a8e380-bc61-4cf0-954d-bd2b0a6745a5.png)

### How to use

Running the Sudoku_solver.py script will open a simple GUI which will let you enter the numbers from your problem sudoku. It has three buttons: Reset, Solve, Quit.

**Reset** - Clears all input numbers

**Solve** - Solves sudoku and gives solution on the right screen

**Quit** - Closes application

In case the problem sudoku has multiple solutions, the first solution will be displayed in the UI, and remaining solutions can be shown in the terminal if requested by user.

![Screen Shot 2021-08-19 at 4 21 16 PM](https://user-images.githubusercontent.com/54175817/130057261-42b34986-e319-4fea-bdac-91ef711637fc.png)

### Approach

**Manual Approach**: This solves the sudoku using methods similar to human solving. It checks every column, row, then box for missing numbers and fills it in if there is only one possible option. It failes for difficult sudokus that would require guessing by the solver.

**Backtracking Approach**: This  is a recursive approach to solve a sudoku. It guesses a number for each box and checks at every point if the rules are broken; if so, it *backtracks* and tries a different number. It is more thorough in the solving process and also identifies if there are multiple possible solutions. However, the time taken for this approach can be quite large.

**Combined Approach**: In this program, a combined approach is taken where it solves the sudoku to the maximum possible point with the manual approach. When no more numbers can be added, it shifts to the backtracking approach. This ensures that the solving process takes less time than a purely backtracking approach. 

The program also has an option to solve sudoku using only one of the above approaches.

At the end of every solution found the recursive count and number of solutions found are displayed on the terminal.

### Screenshots

Terminal Interaction

![Screen Shot 2021-08-19 at 4 14 26 PM](https://user-images.githubusercontent.com/54175817/130057281-e1e34b20-222c-42b7-a307-f1928b67fe9c.png)

Terminal output for multiple solutions (Here, 3 solutions)

![Screen Shot 2021-08-19 at 4 20 38 PM](https://user-images.githubusercontent.com/54175817/130057273-b3b01cf4-d9da-4ae1-b7e1-897f1a436371.png)

For situation where no solutsion are found

![Screen Shot 2021-08-19 at 4 17 18 PM](https://user-images.githubusercontent.com/54175817/130057285-1e44b7ad-ab3d-43aa-b7d7-794a3a11ef67.png)


