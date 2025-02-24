#include <stdio.h>
#include <stdlib.h>
#include <string.h>



void peak_finder(int arr[]){
    for(int i=1; i<5; i++){
        if(arr[i]>=arr[i-1] && arr[i]>=arr[i+1]){
            printf("%d , ",arr[i]);
        }
    }
}




void insertion_sort(int arr[], int length){
    for(int i = 1; i<length; i++){
        int temp = arr[i];
        int j = i-1;
        while(j>=0 && arr[j]>temp){
            arr[j+1] = arr[j];
            j--;
        }
        arr[j+1] = temp;
    }
}

void bubbleSort(int arr[], int n) {
    int i, j, temp;
    for (i = 0; i < n-1; i++) {
        // Last i elements are already in place
        for (j = 0; j < n-1; j++) {
            if (arr[j] > arr[j+1]) {
                // Swap arr[j] and arr[j+1]
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

void selectionSort(int arr[], int n) {
    int i, j, min_idx, temp;

    
    for (i = 0; i < n-1; i++) {

        min_idx = i;
        for (j = i+1; j < n; j++) {
            if (arr[j] < arr[min_idx]) {
                min_idx = j;
            }
        }

        temp = arr[min_idx];
        arr[min_idx] = arr[i];
        arr[i] = temp;
    }
}
int main(){
    // int arr[] = {15,16,6,8,5,15,16,6,8,5};
    // int len = sizeof(arr) / sizeof(arr[0]);
    int arr[] = {1,3,2,4,1};


    // selectionSort(arr,len);
    // // bubbleSort(arr,len);
    // for(int i =0; i<len; i++){
    //     printf("%d ", arr[i]);
    // }

    peak_finder(arr);
}