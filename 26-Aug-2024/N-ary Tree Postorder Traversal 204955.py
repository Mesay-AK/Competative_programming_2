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

        if not root:
            return []

        stack = [root]
        result = []

        while stack:
            popd = stack.pop()
            for child in popd.children:
                stack.append(child)

            result.append(popd.val)

        return result[::-1]