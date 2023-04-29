def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Find the minimum element in the unsorted part of the array
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the minimum element with the first element of the unsorted part
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


if __name__ == '__main__':
    arr = [25, 31, 29, 12, 42, 10, 55, 2, 5, 74]
    selection_sort(arr)
    print("Sorted array:")
    for i in range(len(arr)):
        print(arr[i], end=" ")