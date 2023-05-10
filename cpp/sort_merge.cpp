/*
Merge Sort:
1. Recursive Algorithm
2. Worst case: O(nlg(n))
3. Break array untill till single element, then start merging in sorted order in a bottom-up approach
4. The last merging step of a merge sort is the most crutial part:
    a. We take two individually sorted array and place a pointer on the first element of each of the two arrays
    b. Create a new array copying the least (in case of ascending order) element of the two pointed values. 
    c. Move this pointer to next element of the array and do not move the other pointer.
    d. Keep on doing this untill all elements of both the arrays are copied to the new array
5. Merge Sort is good for ultra long arrays. For the constant before the O(lg(n)) is very large
6. Merge Sort is Not good for short arrays.
*/



#include<stdlib.h>
#include<stdio.h>
using namespace std;
void merge(int [], int, int, int);

void printArray(int A[], int size)
{
int i;
for (i=0; i < size; i++)
printf("%d ", A[i]);
}

void mergeSort(int arr[], int l, int r)
{
    if (l < r)
        {
        int m = (l + r)/2;
        mergeSort(arr, l, m);
        mergeSort(arr, m+1, r);
        merge(arr, l, m, r);
    }
}

// Merge Function
void merge(int arr[], int l, int m, int r)
{
int i, j, k;
int n1 = m - l + 1;
int n2 = r - m;
int L[n1], R[n2];
for (i = 0; i < n1; i++)
L[i] = arr[l + i];
for (j = 0; j < n2; j++)
R[j] = arr[m + 1+ j];
i = 0;
j = 0;
k = l;
while (i < n1 && j < n2)
{
if (L[i] <= R[j])
{
arr[k] = L[i];
i++;
}
else
{
arr[k] = R[j];
j++;
}
k++;
}
while (i < n1)
{
arr[k] = L[i];
i++;
k++;
}
while (j < n2)
{
arr[k] = R[j];
j++;
k++;
}
}

int main()
{
int arr[] = {47, 54, 84, 4, 50, 87, 55, 34, 12, 79};
int arr_size = sizeof(arr)/sizeof(arr[0]);
printf("Given array:\n");
printArray(arr, arr_size);
mergeSort(arr, 0, arr_size - 1);
printf("\nSorted array:\n");
printArray(arr, arr_size);
return 0;
}