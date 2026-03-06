#include <iostream>
using namespace std;

void insert(int arr[], int data, int pos, int n)
{

    for (int i = n - 1; i != pos - 1; i--)
    {
        cout << i;
        arr[i + 1] = arr[i];
    }
    arr[pos] = data;

    for (int j = 0; j <= n + 1; j++)
    {
        cout << arr[j] << endl;
    }
}

void delete_arr(int arr[], int pos, int n)
{
    for (int i = pos; i <= n - 1; i++)
    {
        arr[i] = arr[i + 1];
    }
    arr[n] = 0;
    for (int j = 0; j <= n - 1; j++)
    {
        cout << arr[j] << endl;
    }
}
int main()
{
    // int arr[100];
    int arr[100] = {0, 1, 2, 3, 4, 5};
    delete_arr(arr, 3, 5);

    // insert(arr, 234, 3, 6);
}