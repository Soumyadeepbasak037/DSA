#include <iostream>
#include <vector>

using namespace std;

bool check_valid(vector<vector<int>> &board, int c, int row, int col)
{
    for (int i = 0; i <= 8; i++)
    {
        // cout << " Row: (" << row << "," << i << ")" << " Col: (" << i << "," << col << ")" << endl;

        if (board[row][i] == c)
        { // duplicates in row
            // cout << "found at row: (" << row << "," << i << ")" << endl;
            return false;
        }
        if (board[i][col] == c)
        { // duplicates in col
            // cout << "found at row: (" << i << "," << col << ")" << endl;
            return false;
        }
        // for rows -> (3*(row/3)) + i
        int rows = (3 * (row / 3)) + (i / 3);
        // cols -> (3*(col/3) + (i%3))
        int cols = ((3 * (col / 3)) + (i % 3));

        if (board[rows][cols] == c)
        {
            return false;
        }
    }
    return true;
}

bool solve(vector<vector<int>> &board)
{
    for (int row = 0; row <= 8; row++)
    {
        for (int col = 0; col <= 8; col++)
        {
            if (board[row][col] == 0)
            {
                for (int i = 1; i <= 9; i++)
                {
                    if (check_valid(board, i, row, col))
                    {
                        board[row][col] = i; // take
                        if (solve(board) == true)
                        {
                            return true;
                        }
                        else
                        {
                            board[row][col] = 0;
                        }
                    }
                }
                return false; // no valid number
            }
        }
    }

    for (int i = 0; i <= 8; i++)
    {
        for (int j = 0; j <= 8; j++)
        {
            cout << board[i][j] << endl;
        }
    }
    return true;
}

// void print_2d_vector()

int main()
{
    vector<vector<int>> board = {
        {5, 3, 0, 0, 7, 0, 0, 0, 0},
        {6, 0, 0, 1, 9, 5, 0, 0, 0},
        {0, 9, 8, 0, 0, 0, 0, 6, 0},

        {8, 0, 0, 0, 6, 0, 0, 0, 3},
        {4, 0, 0, 8, 0, 3, 0, 0, 1},
        {7, 0, 0, 0, 2, 0, 0, 0, 6},

        {0, 6, 0, 0, 0, 0, 2, 8, 0},
        {0, 0, 0, 4, 1, 9, 0, 0, 5},
        {0, 0, 0, 0, 8, 0, 0, 7, 9}};

    // check_valid(board, 2, 5, 7);
    solve(board);
}