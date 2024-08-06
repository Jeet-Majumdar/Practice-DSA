"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
 

Constraints:

0 <= n <= 105
 

Follow up:

It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?
"""

from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        # Dynamic Programming solution
        # O(n)
        dp = [0]
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
              offset = i
            dp.append(1 + dp[i - offset])
            #print(dp, i - offset, offset)
        return dp


        # # O(nlogn) solution
        # def count_bits(x):
        #     c = 0
        #     while x != 0:
        #         c += x % 2
        #         x = x // 2
        #     return c
        
        # res = []
        # for i in range(n + 1):
        #     res.append(count_bits(i))
        # return res
