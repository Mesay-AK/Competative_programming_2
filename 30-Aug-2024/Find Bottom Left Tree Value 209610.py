# Problem: Find Bottom Left Tree Value - https://leetcode.com/problems/find-bottom-left-tree-value/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        track = defaultdict(list)

        def traversing(root, r):
            if not root:
                return
            track[r].append(root.val)
            
            traversing(root.left, r+1)
            traversing(root.right, r+1)


        traversing(root, 0)

        last = 0
        for i in track:
            last = max(last, i)

        value = track[last]

        return value[0]