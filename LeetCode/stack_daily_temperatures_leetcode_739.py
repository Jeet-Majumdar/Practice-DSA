"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 10^5
30 <= temperatures[i] <= 100
"""

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # https://www.youtube.com/watch?v=_ZEvmycwXHs
        # Monotonous Stack (Min)
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        
        res = [0 for i in temperatures]
        stack = []
        for idx, val in enumerate(temperatures):
            while len(stack) and stack[-1][1] < val:
                stack_idx, stack_val = stack.pop()
                diff = idx - stack_idx
                res[stack_idx] = diff
            stack.append((idx, val))
        return res

"""
## My original solution: Takes a little extra time for 2-3 more lines so fails submission time
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # https://www.youtube.com/watch?v=_ZEvmycwXHs
        res = [0 for i in temperatures]
        stack = []
        for idx, val in enumerate(temperatures):
            while len(stack) != 0:
                stack_idx, stack_val = stack[-1]
                if stack_val > val:
                    break
                if stack_val < val:
                    diff = idx - stack_idx
                    res[stack_idx] = diff
                    stack.pop()
            stack.append((idx, val))
        return res
"""

"""
## Lousy Brute force solution: (NOT TIME OPTIMIZED)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for i in temperatures]
        for i in range(0, len(temperatures)):
            count = 0
            for j in range(i+1, len(temperatures)):
                count += 1
                if temperatures[j] > temperatures[i]:                    
                    res[i] = count
                    break
        return res
"""