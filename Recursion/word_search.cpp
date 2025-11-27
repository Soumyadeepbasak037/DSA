#include <iostream>
#include <stdlib.h>
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

bool search(vector<vector<char>> &board, string word, int cur_indx, int row, int col, vector<pair<int, int>> &path, vector<vector<int>> &visited)
{
    vector<pair<int, int>> directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    if (cur_indx == word.length())
    {
        return true;
    }
    for (const auto &p : directions)
    {
        int dx = p.first;
        int dy = p.second;

        int x = row + dx;
        int y = col + dy;

        // checks
        if (x < board.size() && y < board[0].size() && x >= 0 && y >= 0 && board[x][y] == word[cur_indx] && visited[x][y] == false)
        {
            visited[x][y] = true;
            pair<int, int> pos_pair = {x, y};
            path.push_back(pos_pair);
            if (search(board, word, cur_indx + 1, x, y, path, visited))
            {
                print_2d(path);
                return true;
            };
            visited[x][y] = false;
            path.pop_back();
        }
    }
    return false;
}

void solve(vector<vector<char>> &board, string word)
{
    int n = board.size();
    int m = board[0].size();
    vector<vector<int>> visited(n, vector<int>(m, 0));
    vector<pair<int, int>> path;

    for (int i = 0; i < board.size(); i++)
    {
        for (int j = 0; j < board[0].size(); j++)
        {
            if (board[i][j] == word[0])
            {
                visited[i][j] = true;
                path.push_back({i, j});

                search(board, word, 1, i, j, path, visited);
                if (search(board, word, 1, i, j, path, visited))
                    return;

                visited[i][j] = false;
                path.clear();
            }
        }
    }
    cout << "No path found\n";
}
int main()
{
    vector<vector<char>> board = {
        {'A', 'B', 'C', 'E'},
        {'S', 'F', 'C', 'S'},
        {'A', 'D', 'E', 'E'}};

    string word = "ABCCED";
    solve(board, word);
}