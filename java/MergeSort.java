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

import java.util.Arrays;

class MergeSort {

    void mergeSort(int array[], int left, int right) {
        if (left < right) {

            int mid = (left + right) / 2;

            mergeSort(array, left, mid);
            mergeSort(array, mid + 1, right);

            merge(array, left, mid, right);
        }
        }
        
    void merge(int array[], int p, int q, int r) {

    int n1 = q - p + 1;
    int n2 = r - q;

    int L[] = new int[n1];
    int M[] = new int[n2];

    for (int i = 0; i < n1; i++)
        L[i] = array[p + i];
    for (int j = 0; j < n2; j++)
        M[j] = array[q + 1 + j];

    int i, j, k;
    i = 0;
    j = 0;
    k = p;

    while (i < n1 && j < n2) {
        if (L[i] <= M[j]) {
        array[k] = L[i];
        i++;
        } else {
        array[k] = M[j];
        j++;
        }
        k++;
    }

    while (i < n1) {
        array[k] = L[i];
        i++;
        k++;
    }

    while (j < n2) {
        array[k] = M[j];
        j++;
        k++;
    }
    }

    
    public static void main(String args[]) {
    int[] array = {47, 54, 84, 4, 50, 87, 55, 34, 12, 79 };

    MergeSort ob = new MergeSort();
    ob.mergeSort(array, 0, array.length - 1);

    System.out.println("Sorted Array:");
    System.out.println(Arrays.toString(array));
    }
}