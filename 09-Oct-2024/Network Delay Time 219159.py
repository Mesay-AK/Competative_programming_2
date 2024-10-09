# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        costs = [float('inf')] * (n + 1) 
        costs[k] = 0  

        heap = [(0, k)]

        while heap:
            curr_cost, curr_node = heapq.heappop(heap)

            if curr_cost > costs[curr_node]:
                continue

            for neighbor, weight in graph[curr_node]:
                new_cost = curr_cost + weight
                if new_cost < costs[neighbor]:
                    costs[neighbor] = new_cost
                    heapq.heappush(heap, (new_cost, neighbor))


        max_cost = max(costs[1:]) 
        return max_cost if max_cost != float('inf') else -1
