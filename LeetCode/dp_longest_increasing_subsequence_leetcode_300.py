"""
Given an integer array nums, return the length of the longest strictly increasing 
subsequence
.

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
 

Constraints:

1 <= nums.length <= 2500
-10^4 <= nums[i] <= 10^4
 

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
"""

from typing import List

class Solution:
    def findClosestBinarySearch(self, data, val):
        highIndex = len(data)-1
        lowIndex = 0
        while highIndex > lowIndex:
                index = (highIndex + lowIndex) // 2
                sub = data[index]
                if data[lowIndex] == val:
                        return [lowIndex, lowIndex]
                elif sub == val:
                        return [index, index]
                elif data[highIndex] == val:
                        return [highIndex, highIndex]
                elif sub > val:
                        if highIndex == index:
                                return sorted([highIndex, lowIndex])
                        highIndex = index
                else:
                        if lowIndex == index:
                                return sorted([highIndex, lowIndex])
                        lowIndex = index
        return sorted([highIndex, lowIndex])
            
            
    def lengthOfLIS(self, nums: List[int]) -> int:
        # https://www.youtube.com/watch?v=0wT67DOzqBg
        # https://www.youtube.com/watch?v=22s1xxRvy28
        # Patience sorting
        # https://www.youtube.com/watch?v=XhzQHpGcQg4
        # https://www.youtube.com/watch?v=TocJOW6vx_I
        # O(n log n)
        
        res = 1
        dp = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > dp[-1]:
                dp.append(nums[i])
            else:
                replace_idx = self.findClosestBinarySearch(dp, nums[i])[1]
                dp[replace_idx] = nums[i]
            res = len(dp)
        
        return res

"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # https://www.youtube.com/watch?v=cjWnW0hdF1Y
        # O(n^2)
        lis = [1] * len(nums)
        lis[len(nums) - 1] = 1
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    lis[i] = max(lis[i], 1 + lis[j])
        return max(lis)
"""