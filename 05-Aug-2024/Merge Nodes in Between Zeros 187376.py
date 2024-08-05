# Problem: Merge Nodes in Between Zeros - https://leetcode.com/problems/merge-nodes-in-between-zeros

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sums = head
        current = head.next
        total = 0

        while current and current.next:
            if current.val == 0:
                sums.val = total
                total = 0
                sums.next = current
                sums = sums.next
            else:
                total += current.val

            current = current.next
            if not current.next:
                sums.val = total
                sums.next = current.next
                return head
            
        