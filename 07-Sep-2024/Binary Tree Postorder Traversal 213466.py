# Problem: Binary Tree Postorder Traversal - https://leetcode.com/problems/binary-tree-postorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []

        stack = []
        l = []
        stack.append(root)

        while(len(stack) != 0):
            root = stack[-1]
            l.insert(0,root.val)
            stack.pop()

            if(root.left != None):
                stack.append(root.left)

            if(root.right != None):
                stack.append(root.right)
                
        return l
               
            
        



        
            

    #     l=[]
    #     self.recursivePostOrder(root,l)
    #     return l
    # def recursivePostOrder(self,root,l):
    #     if root!= None:
    #         self.recursivePostOrder(root.left,l)
    #         self.recursivePostOrder(root.right,l)
    #         l.append(root.val)
