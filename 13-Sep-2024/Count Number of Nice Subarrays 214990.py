# Problem: Count Number of Nice Subarrays - https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        right = 0
        result = 0

        while right < n:
            while right < n and k > 0:
                if nums[right] % 2 != 0:
                    k -= 1
                right += 1

            i = left
            j = right

            while left < right and nums[left] % 2 == 0:
                left += 1

            while right < n and nums[right] % 2 == 0:
                right += 1

            if k == 0:
                result += (left - i + 1) * (right - j + 1)

            left += 1
            k += 1

        return result