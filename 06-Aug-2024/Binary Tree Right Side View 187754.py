# Problem: Binary Tree Right Side View - https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root: return []
        
        track = {}
        
        def dfs(root, level):
            if not root:
                return
            
            if level not in track:
                track[level] = root.val

            dfs(root.right, level + 1)
            dfs(root.left, level + 1)

        dfs(root, 0)
        
        result = []
        for v in track.values():
            result.append(v)
        return result
                
            