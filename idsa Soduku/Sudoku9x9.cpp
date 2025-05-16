#include <iostream>
#include <vector>

using namespace std;

const int SIZE = 9;

// Function to print the Sudoku grid
void printGrid(vector<vector<int>>& grid) {
    for (int i = 0; i < SIZE; ++i) {
        for (int j = 0; j < SIZE; ++j) {
            cout << grid[i][j] << " ";
        }
        cout << endl;
    }
}

// Function to check if it's safe to place 'num' in the given row and column
bool isSafe(vector<vector<int>>& grid, int row, int col, int num) {
    // Check the row and column
    for (int i = 0; i < SIZE; ++i) {
        if (grid[row][i] == num || grid[i][col] == num) {
            return false;
        }
    }

    // Check the 3x3 subgrid
    int subgridSize = 3;
    int startRow = row - row % subgridSize;
    int startCol = col - col % subgridSize;
    for (int i = 0; i < subgridSize; ++i) {
        for (int j = 0; j < subgridSize; ++j) {
            if (grid[i + startRow][j + startCol] == num) {
                return false;
            }
        }
    }

    return true;
}

// Function to solve Sudoku using backtracking
bool solveSudoku(vector<vector<int>>& grid) {
    for (int row = 0; row < SIZE; ++row) {
        for (int col = 0; col < SIZE; ++col) {
            if (grid[row][col] == 0) {
                for (int num = 1; num <= SIZE; ++num) {
                    if (isSafe(grid, row, col, num)) {
                        grid[row][col] = num;
                        if (solveSudoku(grid)) {
                            return true;
                        }
                        grid[row][col] = 0;
                    }
                }
                return false;
            }
        }
    }
    return true;
}

int main() {
    vector<vector<int>> grid(SIZE, vector<int>(SIZE, 0));

    // Read the Sudoku puzzle from stdin
    for (int i = 0; i < SIZE; ++i) {
        for (int j = 0; j < SIZE; ++j) {
            cin >> grid[i][j];
        }
    }

    // Solve the Sudoku puzzle
    if (solveSudoku(grid)) {
        // Print the solution
        printGrid(grid);
    } else {
        cout << "No Solution" << endl;
    }

    return 0;
}
