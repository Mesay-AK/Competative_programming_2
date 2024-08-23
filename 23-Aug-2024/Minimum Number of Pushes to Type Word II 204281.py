# Problem: Minimum Number of Pushes to Type Word II - https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

class Solution:
    def minimumPushes(self, word: str) -> int:

        count = defaultdict(int)
        for i in word:
            count[i] += 1

        many = 0

        key = 2
        times = 1
        for i in sorted(count.items(), key= lambda x: x[1], reverse= True):

            many += i[1] * times
            key += 1

            if key > 9:
                key = 2
                times += 1

        return many
