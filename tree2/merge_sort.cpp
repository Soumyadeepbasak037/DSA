#include <iostream>
#include <algorithm>
using namespace std;

void merge(int arr[], int low, int mid, int high)
{
    int i = low;
    int j = mid + 1;
    int k = low;
    int temp[100];
    while (i <= mid && j <= high)
    {
        if (arr[i] < arr[j])
        {
            temp[k] = arr[i];
            i++;
        }
        else
        {
            temp[k] = arr[j];
            j++;
        }
        k++;
    }
    while (i <= mid - 1)
    {
        temp[k] = arr[i];
        i++;
        k++;
    }
    while (j <= high)
    {
        temp[k] = arr[j];
        j++;
        k++;
    }

    for (int x = low; x <= high; x++)
    {
        arr[x] = temp[x];
    }
}

void mergesort(int arr[], int low, int high)
{
    if (low < high)
    {
        int mid = (low + high) / 2;
        mergesort(arr, low, mid);
        mergesort(arr, mid + 1, high);
        merge(arr, low, mid, high);
    }
}

int main()
{
    int arr[3] = {2, 3, 4};
    mergesort(arr, 0, 2);
    for (int x = 0; x <= 2; x++)
    {
        cout << arr[x] << " ";
    }
}
