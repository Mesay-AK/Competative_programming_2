# Problem: Minimum Number of Vertices to Reach All Nodes - https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        incoming = defaultdict(int)
        nodes = set()

        for a, b in edges:
            incoming[b] += 1
            nodes.add(a)
            nodes.add(b)

        result = []
        
        for value in nodes:
            if value not in incoming:
                result.append(value)

        return result