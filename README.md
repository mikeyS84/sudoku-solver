# sudoku-solver
A Python Sudoku solver using a recursive backtracking algorithm.

## How to Use
1. Clone the repo:
git clone https://github.com/mikeyS84/sudoku-solver.git

2. Run the example:
python example.py

3. To use on your own 9x9 numpy array:
```python
from solver import sudoku_solver
solution = sudoku_solver(your_board)
```

If the board is unsolvable, it returns a board filled with -1.
