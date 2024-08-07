"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

class Solution:
    def spiralOrder(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        t = m*n

        r_b = 0
        r_e = m
        c_b = 0
        c_e = n

        res = []
        count = 0
        row = 0
        col = 0
        while True: 
            if c_b == c_e or r_b == r_e or count == t:
              break
            r = r_b
            for c in range(c_b, c_e):
                if c_b == c_e or r_b == r_e or count == t:
                  break
                count += 1
                res.append(matrix[r][c])
            c = c_e - 1
            for r in range(r_b + 1, r_e):
                if c_b == c_e or r_b == r_e or count == t:
                  break
                count += 1
                res.append(matrix[r][c])
            r = r_e - 1
            for c in range(c - 1, c_b-1, -1):
                if c_b == c_e or r_b == r_e or count == t:
                  break
                count += 1
                res.append(matrix[r][c])
            c = c_b
            for r in range(r - 1, r_b, -1):
                if c_b == c_e or r_b == r_e or count == t:
                  break
                count += 1
                res.append(matrix[r][c])
            c_b += 1 
            c_e -= 1
            r_b += 1
            r_e -= 1
        
        return res