#include <iostream>
#include <vector>
using namespace std;

int main()
{
   int col;
   int row;
   cin >> col >> row ;
   vector<vector<int>> grid(row , vector<int> (col, 0));
    
   // TASK 2
   
   int a_x , a_y , h_x , h_y ,  b_x , b_y , t_x , t_y ;
   cin >> a_x >> a_y >> h_x >> h_y >>  b_x >> b_y >> t_x >> t_y ;
   
   for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < col; j++)
        {
            grid[a_y][a_x] = 5;
            grid[h_y][h_x] = 1;
            grid[b_y][b_x] = 1;
            grid[t_y][t_x] = 1;
            cout << grid[i][j] << " ";
        }    
        cout << endl;
    }
   
    return 0;
}