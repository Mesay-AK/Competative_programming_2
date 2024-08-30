# Problem: Binary Tree Preorder Traversal - https://leetcode.com/problems/binary-tree-preorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            result = []
            stack = []
            stack.append(root)
            while stack:
                curr = stack[-1]
                stack.pop()
                if curr.right:
                    stack.append(curr.right)
                
                if curr.left:
                    stack.append(curr.left)

                result.append(curr.val)
            return result

