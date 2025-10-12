#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int recursion(int indx1, int indx2, string s1, string s2, vector<vector<int>> &dp)
{
    if (indx1 < 0 || indx2 < 0)
    {
        return 0;
    }

    if (dp[indx1][indx2] != -1)
    {
        return dp[indx1][indx2];
    }

    if (s1[indx1] == s2[indx2]) // match
    {
        return dp[indx1][indx2] = 1 + recursion(indx1 - 1, indx2 - 1, s1, s2, dp);
    }

    return dp[indx1][indx2] = max(recursion(indx1 - 1, indx2, s1, s2, dp), recursion(indx1, indx2 - 1, s1, s2, dp));
}

int main()
{
    string s1 = "AGGTAB";
    string s2 = "GXTXAYB";
    vector<vector<int>> dp(s1.size(), vector<int>(s2.size(), -1));

    cout << recursion(s1.size() - 1, s2.size() - 1, s1, s2, dp) << endl;

    for (int i = 0; i < s1.size(); i++)
    {
        for (int j = 0; j < s2.size(); j++)
        {
            cout << " " << dp[i][j] << " ";
        }
        cout << "\n";
    }
}