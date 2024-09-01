"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
 
Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""

# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # Two pointer method
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pt1 = head
        pt2 = head
        dummy = None
        # giving heads-start to the second pointer by n amount
        while n != -1:
            if pt2 is None:
                return None
            pt2 = pt2.next
            n -= 1
        
        # Check when pt2 hits end. It is then pt1 will be at the n-th node
        while pt2 is not None:
            dummy = pt1
            pt1 = pt1.next
            pt2 = pt2.next
        
        pt1.next = pt1.next.next
        return head


