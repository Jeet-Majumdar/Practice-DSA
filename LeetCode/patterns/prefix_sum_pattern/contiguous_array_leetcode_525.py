"""
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

 

Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
 

Constraints:

1 <= nums.length <= 10^5
nums[i] is either 0 or 1.
"""

from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # Ref Video: https://www.youtube.com/watch?v=agB1LyObUNE
        # 111 000
        # How to know to shrink window or increase?
        # Have to split, thus recursive and worse than O(n^2)

        # Not every result starts at beginning, e.g. 111 00

        # is it possible to know exactly where the first 1 was, and verify that after it
        # count[1] == count[0]

        # map each index to pair (count[0], count[1])
        # Use diff between counts for O(1) lookup of what we need
        
        zero, one = 0, 0
        res = 0
        diff_index = {} # diff --> index   [diff=count[1]-count[0]]
        
        for i, n in enumerate(nums):
            if n == 0:
                zero += 1
            else:
                one += 1
        
            if one - zero not in diff_index:
                diff_index[one - zero] = i
            
            if one == zero:
                res = one + zero # This is definitely the longest subarray at this point
            else:
                idx = diff_index[one - zero]
                res = max(res, i - idx)
        
        return res
