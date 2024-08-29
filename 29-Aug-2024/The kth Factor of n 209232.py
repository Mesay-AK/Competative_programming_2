# Problem: The kth Factor of n - https://leetcode.com/problems/the-kth-factor-of-n/

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        result = {1, n}

        div = 2
        while div * div <= n:
            if n % div == 0:
                result.add(div)
                result.add(n//div)

            div += 1

        result = list(result)
        result.sort()

        return result[k - 1] if len(result) >= k else -1
