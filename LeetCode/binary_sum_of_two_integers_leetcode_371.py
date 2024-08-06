"""
Given two integers a and b, return the sum of the two integers without using the operators + and -.

 

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = 2, b = 3
Output: 5
 

Constraints:

-1000 <= a, b <= 1000
"""
class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Time O(1)
        # Space O(1)

        # Constraints: -1000 <= a, b <= 1000

        mask = 0xffffffff # binary of int -1

        while (b & mask) > 0:
            a, b = (a ^ b), (a & b) << 1
        
        return (a & mask) if b > 0 else a