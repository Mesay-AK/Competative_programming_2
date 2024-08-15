# Problem: Step-By-Step Directions From a Binary Tree Node to Another - https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], start: int, dest: int) -> str:

        graph = defaultdict(lambda: [None, None, None])
        def dfs(root, parent):

            if root.left:
                graph[root.val][0] = root.left.val
                dfs(root.left, root)

            if root.right: 
                graph[root.val][1] = root.right.val
                dfs(root.right, root)

            if parent:
                graph[root.val][2] = parent.val
        
        def bfs(start, dest):

            queue = deque()
            queue.append((start, ""))
            step = ["L", "R", "U"]
            visited = set()

            while queue:

                node, path = queue.popleft()
                if node == dest:
                    return path

                visited.add(node)
                for i, nei in enumerate(graph[node]):

                    if nei and nei not in visited:
                        queue.append((nei, path + step[i]))

                        
        dfs(root, None)
        return bfs(start, dest)
        
        