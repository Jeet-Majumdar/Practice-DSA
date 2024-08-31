"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 10^4.
"""

# Definition for singly-linked list.

from typing import List, Optional

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                mergedLists.append(self.mergeTwoLists(l1, l2))
            lists = mergedLists
        return lists[0]
    
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
