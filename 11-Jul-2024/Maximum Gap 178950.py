# Problem: Maximum Gap - https://leetcode.com/problems/maximum-gap/

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        
        max_value, min_value = max(nums), min(nums)
        size = max(1, (max_value - min_value) // (n - 1))
        num_ = (max_value - min_value) // size + 1
     
        buckets = [[float('inf'), float('-inf')] for _ in range(num_)]
        for num in nums:
            
            bucket_index = (num - min_value) // size
            buckets[bucket_index][0] = min(buckets[bucket_index][0], num)
            buckets[bucket_index][1] = max(buckets[bucket_index][1], num)
        
    
        max_diff = 0
        prev_max = buckets[0][1]
        for i in range(1, num_):
            if buckets[i][0] == float('inf'):
                continue
            max_diff = max(max_diff, buckets[i][0] - prev_max)
            prev_max = buckets[i][1]
        
        return max_diff