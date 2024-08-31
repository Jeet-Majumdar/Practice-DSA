"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""

# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2
        head = None
        res = None
        while head1 is not None and head2 is not None:
            if head1.val < head2.val:
                val = head1.val
                head1 = head1.next
            else:
                val = head2.val
                head2 = head2.next
            
            temp = ListNode(val)
            if head is None:                
                head = temp
                res = head
            else:
                head.next = temp
                head = head.next
        
        while head1 is not None:
            temp = ListNode(head1.val)
            if head is None:                
                head = temp
                res = head
            else:
                head.next = temp
                head = head.next
            head1 = head1.next
        
        while head2 is not None:
            temp = ListNode(head2.val)
            if head is None:                
                head = temp
                res = head
            else:
                head.next = temp
                head = head.next
            head2 = head2.next
        
        return res