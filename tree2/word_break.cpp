#include <stdlib.h>
#include <iostream>
#include <vector>
using namespace std;

bool check_valid(vector<string> arr, vector<bool> &temp, string substring)
{

    for (int i = 0; i < arr.size(); i++)
    {
        if (arr[i] == substring)
        {
            temp[i] = false;
            return true;
        }
        else
        {
            return false;
        }
    }
}

bool backtrack(string s, int start, vector<string> arr, vector<bool> temp)
{
    for (auto elem : temp)
    {
        if (elem == true)
        {
            return true;
        }
    }
    if (start == s.size() + 1)
    {
        return;
    }

    for (int end = start + 1; end <= s.size(); end++)
    {
        string substring = s.substr(start, start - end);
        if (check_valid(arr, temp, substring))
        {
            backtrack(s, end, arr, temp);
        }
    }
}

int main()
{
    vector<string> dict;
    dict = {"leet", "code"};
}