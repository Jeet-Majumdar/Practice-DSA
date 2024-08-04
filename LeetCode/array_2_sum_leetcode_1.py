"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_sort = [i for i in nums]
        nums_sort.sort()
        i = 0
        j = len(nums) - 1
        while i<j:
            if (nums_sort[i] + nums_sort[j]) > target:
                j = j - 1
            elif (nums_sort[i] + nums_sort[j]) < target:
                i = i + 1
            else:
                a = nums_sort[i]
                b = nums_sort[j]
                s = []
                for k in range(len(nums)):
                    if nums[k] == a or nums[k] == b:
                        s.append(k)
                s.sort()
                return s

