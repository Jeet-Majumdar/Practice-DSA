
'''
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
'''

def merge_sort(array, start, end):
    if start < end:
        middle = (start + end) // 2
        merge_sort(array, start, middle)
        merge_sort(array, middle+1, end)
        merge_array_operation(array, start, middle, end)

def merge_array_operation(arr, start, middle, end):
    pointer_1 = start
    pointer_2 = middle+1
    sorted_arr = []
    while pointer_1 <= middle and pointer_2 <= end:
        if arr[pointer_1] <= arr[pointer_2]:
            sorted_arr.append(arr[pointer_1])
            pointer_1 = pointer_1 + 1
        else:
            sorted_arr.append(arr[pointer_2])
            pointer_2 = pointer_2 + 1
    while pointer_1 <= middle:
        sorted_arr.append(arr[pointer_1])
        pointer_1 = pointer_1 + 1
    while pointer_2 <= end:
        sorted_arr.append(arr[pointer_2])
        pointer_2 = pointer_2 + 1
    # Copy content of sorted array to the original array.
    # DO NOT replace arr object coz then it will forget the older reference to the bigger array and will store the object of newly created sorted_list
    j = 0
    for i in range(start, end+1):
        arr[i] = sorted_arr[j]
        j = j + 1
    return sorted_arr


if __name__ == '__main__':
    a = [4, 5,  7, 1, 55, 24, 2, 9]
    merge_sort(a, 0, len(a)-1)
    print(a)