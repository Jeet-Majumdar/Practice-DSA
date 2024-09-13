"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Example 2:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 3:
Input: nums = [1,2,3]
Output: 3
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000
"""

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Idea ref: https://www.youtube.com/watch?v=5bxF0MJ1oM0
        def custom_rob(arr):
            if len(arr) == 1:
                return arr[0]
            elif len(arr) == 2:
                return max(arr[0], arr[1])
            
            max_val = [0 for i in range(len(arr))]
            max_val[0] = arr[0]
            max_val[1] = max(arr[0], arr[1])

            for i in range(2, len(arr)):
                l_1 = max_val[i - 2] + arr[i]
                l_2 = max_val[i - 1]
                max_val[i] = max(l_1, l_2)
            
            return max_val[-1]
        
        if len(nums) == 1:
                return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])

        arr1 = [nums[i] for i in range(0, len(nums) - 1)] # from 0 -> n-1
        arr2 = [nums[i] for i in range(1, len(nums))] # from 1 -> n
        
        res_arr1 = custom_rob(arr1)
        res_arr2 = custom_rob(arr2)
        return max(res_arr1, res_arr2)