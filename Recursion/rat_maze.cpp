#include <iostream>
#include <vector>
#include <utility>
using namespace std;

void print_2d(vector<pair<int, int>> &arr)
{
    for (const auto &elem : arr)
    {
        cout << "{" << elem.first << "," << elem.second << "}" << endl;
    }
    cout << "----" << endl;
}

bool dfs(vector<vector<char>> &board, vector<pair<int, int>> &path, vector<vector<int>> &visited, int row, int col, pair<int, int> target)
{
    vector<pair<int, int>> directions = {{}, {}, {}, {}};
    // base case
    if (row == target.first && col == target.second)
    {
        return true;
    }
    for (auto const direction : directions)
    {
        int dx = direction.first;
        int dy = direction.second;

        int x = row + dx;
        int y = col + dy;

        if (x >= 0 && y >= 0 && x < board.size() && y < board[0].size() && visited[x][y] != true && board[x][y] != '#')
        {
            visited[x][y] = true;
            path.push_back({x, y});
            if (dfs(board, path, visited, x, y, target))
            {
                print_2d(path);
                return true;
            }
            visited[x][y] = false;
            path.pop_back();
        }
    }
    return false;
}
int main() {}