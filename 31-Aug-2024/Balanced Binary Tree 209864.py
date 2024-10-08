# Problem: Balanced Binary Tree - https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def dfs (node):

            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if left < 0 or right < 0:
                return -1

            elif abs(left - right) > 1:
                return -1

            return max(left, right)+1

        return dfs(root) >= 0
