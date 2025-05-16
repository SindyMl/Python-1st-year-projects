#include <iostream>
#include <vector>
#include <set>

using namespace std;

const int SIZE = 5;
const set<char> sudoku_valid_characters = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};

// Function to print the Sudoku grid
void printGrid(vector<vector<char>>& grid) {
    for (int i = 0; i < SIZE; ++i) {
        for (int j = 0; j < SIZE; ++j) {
            cout << grid[i][j] << " ";
        }
        cout << endl;
    }
}

// Function to check if it's safe to place 'num' in the given row and column
bool isSafe(vector<vector<char>>& grid, int row, int col, char num) {
    // Check the row and column
    for (int i = 0; i < SIZE; ++i) {
        if (grid[row][i] == num || grid[i][col] == num) {
            return false;
        }
    }

    return true;
}

// Function to solve Sudoku using backtracking
bool solveSudoku(vector<vector<char>>& grid) {
    for (int row = 0; row < SIZE; ++row) {
        for (int col = 0; col < SIZE; ++col) {
            if (grid[row][col] == '0') {
                for (char num : sudoku_valid_characters) {
                    if (isSafe(grid, row, col, num)) {
                        grid[row][col] = num;
                        if (solveSudoku(grid)) {
                            return true;
                        }
                        grid[row][col] = '0';
                    }
                }
                return false;
            }
        }
    }
    return true;
}

int main() {
    vector<vector<char>> grid = {{'0', '0', '0', '0', '0'},
                                 {'0', '0', '0', '0', '0'},
                                 {'0', '0', '0', '0', '0'},
                                 {'0', '0', '0', '0', '0'},
                                 {'0', '0', '0', '0', '0'}};

    if (solveSudoku(grid)) {
        // The puzzle is solved
        printGrid(grid);
    } else {
        // The puzzle has no solution
        cout << "No Solution" << endl;
    }

    return 0;
}
