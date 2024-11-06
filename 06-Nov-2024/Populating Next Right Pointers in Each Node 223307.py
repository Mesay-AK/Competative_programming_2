# Problem: Populating Next Right Pointers in Each Node - https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        queue = deque()
        queue.append([0, root])

        while queue:

            for i in range(len(queue)):
                level, node = queue.popleft()

                if queue and queue[0][0] == level:
                    node.next = queue[0][1]

                if node.left:
                    queue.append([level + 1, node.left])
                if node.right:
                    queue.append([level + 1, node.right])
                    

        return root
