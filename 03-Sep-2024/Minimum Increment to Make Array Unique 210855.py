# Problem: Minimum Increment to Make Array Unique - https://leetcode.com/problems/minimum-increment-to-make-array-unique/

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:

        # use a counter to count the number of each number
        # use a variable to store the largest number in the list
        # use a variable to store the number of repetitions the list has
        # prepare the moves variable
        # store the sum of the largest number and the repitiion in a varible
        # iterate through the number and the counter to update the current and the passed variable
        # in each iteration add the passed number in to the moves variable
        
        count = Counter(nums)
        largest = max(count)
        reptitions = 0
        for rep in count.values():
            reptitions += (rep-1)

        maxim = reptitions + largest

        moves = 0
        passed = 0

        for i in range(maxim + 1 ):

            current = count[i] + passed
            if current >= 1:
                moves += ((current-1)) 
                passed = (current - 1) 

        return moves