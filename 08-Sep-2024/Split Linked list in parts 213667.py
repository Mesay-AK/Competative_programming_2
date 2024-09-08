# Problem: Split Linked list in parts - https://leetcode.com/problems/split-linked-list-in-parts/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        result = []
        
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next

        breaking = (count //k)
        broken = count % k
        
        prev = None
        curr = head
        for i in range(k):
            result.append(curr)
            for j in range(breaking):
                if curr:
                    prev = curr
                    curr = curr.next
                
            if curr and broken:
                prev = curr
                curr = curr.next
                broken -= 1
            if prev:
                prev.next = None  

        return result


