'''
Shell Sort
(after Donald Shell)

1. Improved Insertion Sort
2. Can be applied to Bubble Sort
3. Works very well for medium sized arrays having elements upto a few thousands
4. Instead of sorting the whole array, we solve a part of the array and pretend that the other elements do not exist
    (for example every 5th element)
5. After we are done with the above set of elements, we move the index by one. (Moving the period by one)
6. We select the interval/gap between elements? 
    We do that via Knuth Sequence. [h = 3h + 1]
    So h = {1, 4, 13, 40, ..., } till h < data.length
    These intervals are choosen in the reverse order.

'''

def ShellSort(arr):
    h = [1]
    while (3*h[-1] + 1) < len(arr):
        h.append(3*h[-1] + 1)
    h.reverse()

    n = len(arr)
    for i in h:
        for j in range(i, n):
            temp = arr[j]
            k = j
            while  k >= i and arr[k-i] >temp:
                arr[k] = arr[k-i]
                k -= i
            arr[k] = temp
            

if __name__ == '__main__':
    arr = [25, 31, 29, 12, 42, 10, 55, 2, 5, 74]
    print(arr)
    ShellSort(arr)
    print()
    print(arr)



