'''
Lexicographical Ordering

1. Find largest i such that a[i-1] < a[i]
2. Find largest j such that a[i-1] < a[j] from j in range (i-1, len(a))
3. Interchange a[i-1] and a[j]
4. Reverse order of digit a[i], a[i+1], ... a[n]

'''

def LexiPermutation(a):
    if len(a) < 2:
        return a[::-1]

    inverse_point = len(a) - 1

    while inverse_point >= 0 and a[inverse_point-1] > a[inverse_point]:
        inverse_point = inverse_point - 1 

    inverse_point = inverse_point - 1 
    if inverse_point < 0:
        return []
    
    for i in reversed(range(inverse_point, len(a))):
        if a[i] > a[inverse_point]:
            a[i], a[inverse_point] = a[inverse_point], a[i]
            break
    
    a[inverse_point + 1:] = reversed(a[inverse_point + 1:])
    return a

l = [8, 4, 9, 6, 5, 2, 1]
print(l)
print(LexiPermutation(l))

