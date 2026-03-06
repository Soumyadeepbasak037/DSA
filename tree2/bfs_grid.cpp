#include <vector>
using namespace std;
#include <iostream>
#include <queue>

using namespace std;

class Grid
{
public:
    int rows;
    int cols;
    vector<vector<int>> grid;

    Grid(int r, int c)
    {
        this->rows = r;
        this->cols = c;
        this->grid = vector<vector<int>>(r, vector<int>(c, 0));
    }
    void print_grid()
    {
        for (int i = 0; i < rows; i++)
        {
            for (int j = 0; j < cols; j++)
            {
                cout << grid[i][j];
            }
            cout << endl;
        }
    }

    //(stopi,stopj) = target
    vector<pair<int, int>> shortest_path(pair<int, int> target)
    {
        vector<vector<int>> visited(rows, vector<int>(cols, 0));
        // up down left right
        vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        queue<pair<int, int>> q;
        pair<int, int> temp;

        q.push(pair<int, int>{0, 0});

        visited[0][0] = 1;
        while (!q.empty())
        {
            temp = q.front();
            q.pop();

            int x = temp.first;
            int y = temp.second;

            for (int i = 0; i < 4; i++)
            {
                int dx = directions[i].first;
                int dy = directions[i].second;

                int cur_x = x + dx;
                int cur_y = y + dy;

                if (cur_x == target.first && cur_y == target.second)
                {
                    cout << "lol" << endl;
                }

                if (check_valid(cur_x, cur_y, visited))
                {
                    q.push(pair<int, int>{cur_x, cur_y});
                    visited[cur_x][cur_y] = 1;
                }
            }
        }
        return {};
    }

private:
    bool check_valid(int cur_x, int cur_y, const vector<vector<int>> &visited)
    {
        if (cur_x < 0 || cur_y < 0 || cur_x >= rows || cur_y >= cols || visited[cur_x][cur_y] == 1 || grid[cur_x][cur_y] == 0)
        {
            return false;
        }
        return true;
    }
};

int main()
{
}