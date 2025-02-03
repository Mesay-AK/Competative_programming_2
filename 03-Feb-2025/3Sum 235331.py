# Problem: 3Sum - https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()

        for i in range(len(nums)):   

            j = i + 1
            k = len(nums) - 1

            while j < k:
                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1

                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1

                else:
                    if (nums[i], nums[j], nums[k]) not in result:
                        result.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1

        return list(result)


