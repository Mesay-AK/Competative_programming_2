# Problem: Maximum Number of Achievable Transfer Requests - https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/description/

class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        m = len(requests)
        max_count = 0

        for mask in range(1 << m):
            balance = [0] * n
            count = 0
            for i in range(m):
                if (mask >> i) & 1: 
                    from_i, to_i = requests[i]
                    balance[from_i] -= 1
                    balance[to_i] += 1
                    count += 1
            if all(b == 0 for b in balance):
                max_count = max(max_count, count)

        return max_count
