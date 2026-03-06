#include <iostream>
#include <algorithm>
using namespace std;

int partition(int arr[], int low, int high)
{
    int p = arr[low];
    int i = low - 1;
    int j = high + 1;

    while (true)
    {
        do
        {
            i++;
        } while (arr[i] < p);

        do
        {
            j--;
        } while (arr[j] > p);

        if (i >= j)
        {
            return j;
        }
        swap(arr[i], arr[j]);
    }
}

void quicksort(int arr[], int high, int low)
{
    if (low < high)
    {
        int p = partition(arr, low, high);
        quicksort(arr, low, p);
        quicksort(arr, p + 1, high);
    }
}
int main() {}