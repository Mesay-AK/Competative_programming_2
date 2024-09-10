# Problem: Insert Greatest Common Divisors in Linked List - https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head
        
        while curr and curr.next:
            gcd_ = gcd(curr.val, curr.next.val)
            new = ListNode(gcd_)
            new.next = curr.next
            curr.next = new

            curr = new.next

        return head

