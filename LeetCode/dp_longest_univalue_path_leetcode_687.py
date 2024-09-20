"""
Given the root of a binary tree, return the length of the longest path, where each node in the path has the same value. This path may or may not pass through the root.

The length of the path between two nodes is represented by the number of edges between them.

 

Example 1:
Input: root = [5,4,5,1,1,null,5]
Output: 2
Explanation: The shown image shows that the longest path of the same value (i.e. 5).

Example 2:
Input: root = [1,4,5,4,4,null,5]
Output: 2
Explanation: The shown image shows that the longest path of the same value (i.e. 4).
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-1000 <= Node.val <= 1000
The depth of the tree will not exceed 1000.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        ## Ref Video: https://www.youtube.com/watch?v=cwYVhyl2A1s

        self.res = 0

        def dfs(node):
            if node is None:
                return 0
            
            leftChild = dfs(node.left)
            rightChild = dfs(node.right)
            if node.left and node.val == node.left.val:
                leftChild = leftChild + 1
            if node.right and node.val == node.right.val:
                rightChild = rightChild + 1
            
            nodeVal = leftChild + rightChild
            self.res = max(self.res, nodeVal)
            
            # Return the max chain length from this node
            return max(leftChild, rightChild)
        
        dfs(root)
        return self.res
            
        