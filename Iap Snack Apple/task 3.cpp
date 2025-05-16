#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int col;
    int row;
    cin >> col >> row;
    vector<vector<int>> grid(row, vector<int>(col, 0));

    // TASK 2

    int a_x, a_y, N, h_x, h_y, b_x, b_y, t_x, t_y;
    cin >> a_x >> a_y;
    grid[a_y][a_x] = 5;
    cin  >> N;
    int count = 1;

    for (int snake = 0; snake < N; snake++)
    { 
        cin >> h_x >> h_y >> b_x >> b_y >> t_x >> t_y;
        grid[h_y][h_x] = count;
        grid[b_y][b_x] = count;
        grid[t_y][t_x] = count;
        count = count + 1;
    }    
            
    for (int i = 0; i < row;i++)
    {
        for (int j = 0; j < col;j++)
        {  
            cout << grid[i][j] << " ";  
        } 
        cout << endl;
    }
            

    return 0;
}
