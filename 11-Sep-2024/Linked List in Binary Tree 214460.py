# Problem: Linked List in Binary Tree - https://leetcode.com/problems/linked-list-in-binary-tree/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        def findNode(root):
            if not root:
                return False

            if root.val == head.val:
                if checkLink(root, head):
                    return True

            left = findNode(root.left)
            right = findNode(root.right)

            return left or right

        def checkLink(root, node):

            if not node:
                return True

            if not(root and node):
                return False

            if root.val != node.val:
                return False

            left = checkLink(root.left, node.next)
            right = checkLink(root.right, node.next)

            return left or right

        return findNode(root)
            