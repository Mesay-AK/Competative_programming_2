# Problem: Maximum Performance of a Team - https://leetcode.com/problems/maximum-performance-of-a-team/

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        
        team = []
        for eff, spd in zip(efficiency, speed):
            team.append((eff, spd))

        team.sort(reverse = True)

        min_speed = []
        heapq.heapify(min_speed)
        maxim = 0
        speed = 0
        for eff, spd in team:
            speed += spd
            if len(min_speed) == k:
                speed -= heapq.heappop(min_speed)

            heapq.heappush(min_speed, spd)
            maxim = max(maxim, speed * eff)

        return maxim % (10 **9 + 7)