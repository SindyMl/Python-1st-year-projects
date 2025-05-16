#include <iostream>
#include <vector>
using namespace std;

int main()
{
   int col;
   int row;
   cin >> col >> row ;
   vector<vector<int>> grid(row , vector<int> (col, 0));
    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < col; j++)
        {
            cout << grid[i][j] << " ";
        }    
        cout << endl;
    }
   
   
    return 0;
}