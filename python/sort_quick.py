'''
Quick Sort

1. In worst case this takes O(n^2) i.e. absolutely bad
2. Average case this takes O(nlg(n)) time which is as good as merge sort
3. On averge case, better than Merge sort because the constant factor of Quick sort is smaller  
4. Quick sort can be done in-place. That means we dont need any extra memory that is proportional to the data to be sorted.
5. Here we start by pivoting an element in the array (conventionally the last element of the array) and make sure that:
    a. All value to the left of pivot are smaller than pivot
    b. All value to the right are greater than pivot
6. Finding pivot is the crutial step
'''

def QuickSort(arr, start, end):
    if start < end:
        pivot = Partition(arr, start, end)
        QuickSort(arr, start, pivot - 1)
        QuickSort(arr, pivot+1, end)

def Partition(arr, start, end):
    pivot = arr[end]
    i = start
    for j in range(i, end):  # j going from i to one before the end of range given (i.e. end)
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
    arr[i], arr[end] = arr[end], arr[i]
    return i

if __name__ == '__main__':
    a = [4, 5, 7, 1, 55, 24, 2, 9]
    print(a)
    QuickSort(a, 0, len(a)-1)
    print(a)
