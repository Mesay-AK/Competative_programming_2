# Problem: N-ary Tree Postorder Traversal - https://leetcode.com/problems/n-ary-tree-postorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:

        result = []

        def traverse(root):
            if not root:
                return 

            # print(child.val)
            for child in (root.children):
                

                traverse(child)

            result.append(root.val)

        traverse(root)
        return result
        