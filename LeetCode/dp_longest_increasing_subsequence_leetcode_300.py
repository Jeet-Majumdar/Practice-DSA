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
    def lengthOfLIS(self, nums: List[int]) -> int:
        # https://www.youtube.com/watch?v=0wT67DOzqBg
        # https://www.youtube.com/watch?v=22s1xxRvy28
        # O(n log n)
        
        def binary_search(arr, val, start, end):
            if start == end:
                if arr[start] > val:
                    return start
                else:
                    return start+1
        
            if start > end:
                return start
        
            mid = (start+end)/2
            if arr[mid] < val:
                return binary_search(arr, val, mid+1, end)
            elif arr[mid] > val:
                return binary_search(arr, val, start, mid-1)
            else:
                return mid



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