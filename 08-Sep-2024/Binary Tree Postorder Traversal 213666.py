# Problem: Binary Tree Postorder Traversal - https://leetcode.com/problems/binary-tree-postorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        if not root:
            return []
        
        stack = []
        result = []
        last = None
        current = root
        
        while current or stack:
            if current:
                stack.append(current)
                current = current.left
            else:
                node = stack[-1]
                
                if node.right and last != node.right:
                    current = node.right
                else:
                    result.append(node.val) 
                    last = stack.pop()  
        
        return result
