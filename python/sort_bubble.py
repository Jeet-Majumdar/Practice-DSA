def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

if __name__ == '__main__':
    arr = [25, 31, 29, 12, 42, 10, 55, 2, 5, 74]
    bubble_sort(arr)
    print("Sorted array:")
    for i in range(len(arr)):
        print(arr[i], end=" ")
