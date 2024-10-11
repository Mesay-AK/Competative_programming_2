# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        probability = {i: 0 for i in range(n)}
        probability[start_node] = 1

        graph = defaultdict(list)
        for i in range(len(edges)):
            start, end = edges[i]
            graph[end].append((start, succProb[i]))
            graph[start].append((end, succProb[i]))

        heap = [(-1, start_node)]

        while heap:

            success, node = heapq.heappop(heap)
            success = -success

            if node == end_node:
                return success
            if success < probability[node]:
                continue
            

            for neighbour, likelihood in graph[node]:
                probable = success * likelihood

                if probable > probability[neighbour]:
                    probability[neighbour] = probable
                    heapq.heappush(heap, (-probable, neighbour))

        return probability[end_node]