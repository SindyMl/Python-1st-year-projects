#include <iostream>
#include <vector>
#include <queue>
#include <string>
using namespace std;

struct Location {
    int x, y;
    Location* prev;

    Location(int x, int y, Location* prev) : x(x), y(y), prev(prev) {}
};

const int dx[] = {1, 0, -1, 0}; 
const int dy[] = {0, -1, 0, 1};
const char directions[] = {'v', '<', '^', '>'}; 

void updatePath(vector<vector<char>> &maze, Location *end) {
    while (end->prev != nullptr) {
        if (maze[end->x][end->y] != 'G') {
            maze[end->x][end->y] = '*';
        }
        end = end->prev;
    }
}

bool findShortestPath(vector<vector<char>> &maze, int start_x, int start_y, int goal_x, int goal_y) {
    int m = maze.size();
    int n = maze[0].size();
    vector<vector<bool> > visited(m, vector<bool>(n, false));
    queue<Location*> q;
    q.push(new Location(start_x, start_y, nullptr));
    visited[start_x][start_y] = true;

    while (!q.empty()) {
        Location *current = q.front();
        q.pop();

        if (current->x == goal_x && current->y == goal_y) {
            updatePath(maze, current);
            return true;
        }

        for (int i = 0; i < 4; i++) {
            int new_x = current->x + dx[i];
            int new_y = current->y + dy[i];

            if (new_x >= 0 && new_x < m && new_y >= 0 && new_y < n &&
                maze[new_x][new_y] != 'x' && !visited[new_x][new_y]) {
                q.push(new Location(new_x, new_y, current));
                visited[new_x][new_y] = true;
            }
        }
    }

    return false;
}

int main() {
    int rows, cols;
    cin >> rows >> cols;
    cin.ignore();

    vector<vector<char> > maze(rows, vector<char>(cols));

    int start_row, start_col, goal_row, goal_col;

    for (int i = 0; i < rows; i++) {
        string line;
        getline(cin, line);

        for (int j = 0; j < cols; j++) {
            maze[i][j] = line[j];
            if (maze[i][j] == 'S') {
                start_row = i;
                start_col = j;
            } else if (maze[i][j] == 'G') {
                goal_row = i;
                goal_col = j;
            }
        }
    }

    if (findShortestPath(maze, start_row, start_col, goal_row, goal_col)) {
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                cout << maze[i][j];
            }
            cout << endl;
        }
    } else {
        cout << "No Path" << endl;
    }

    return 0;
}
