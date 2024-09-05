"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [a_i, b_i] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        custom_preq = [[] for i in range(numCourses)]
        for i in prerequisites:
            target = i[0]
            have_to = i[1]
            custom_preq[target].append(have_to)
        visited = set()
        def dfs(course):
            if course in visited:
                return 0
            
            if len(custom_preq[course]) == 0:
                return 1
            
            visited.add(course)
            for i in custom_preq[course]:
                if dfs(i) == 0:
                    return 0
            visited.remove(course)
            custom_preq[course] = []
            return 1
        
        res = 1
        for i in range(numCourses):
            res = res * dfs(i)
        return res
