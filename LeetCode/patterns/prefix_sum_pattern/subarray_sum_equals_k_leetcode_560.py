# Prefix Sums
"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 10^4
-1000 <= nums[i] <= 1000
-10^7 <= k <= 10^7
"""

from typing import List 

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Ref Video: https://www.youtube.com/watch?v=1x91vuYSibw
        
        if not nums:
            return 0
        
        # {prefix_sum - k ==> no_of_times_we_seen_that}
        prefix_dict = collections.defaultdict(int) 
        prefix_dict[0] = 1

        prefix_sum = res = 0

        for i in nums:
            prefix_sum += i

            if prefix_sum - k in prefix_dict:
                res += prefix_dict[prefix_sum - k]
            
            prefix_dict[prefix_sum] += 1
        
        return res

