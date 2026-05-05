#include <stdio.h>
int main() 
    {
    int arr[] = {3, 1, 4, 1, 5, 9};
    int max = arr[0];
    for (int i = 0; i < 6; i++)
    {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    printf("Maximum value is: %d\n", max);
    return 0;
}