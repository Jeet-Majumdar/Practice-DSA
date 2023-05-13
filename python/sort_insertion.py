
'''
Insertion Sort

1. Only differene with Selection Sort is the best case scenerio. Selection Sort = O(n^2), Insertion Sort = O(n)
2. Average Case: O(n^2)
3. Worst Case: O(n^2)

'''

def InsertionSort(arr):
     
    if (n := len(arr)) <= 1:
      return
    for i in range(1, n):
         
        key = arr[i]

        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

if __name__ == '__main__':
    a = [4, 5, 7, 1, 55, 24, 2, 9]
    print(a)
    InsertionSort(a)
    print(a)