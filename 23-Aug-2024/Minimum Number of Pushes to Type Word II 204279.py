# Problem: Minimum Number of Pushes to Type Word II - https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

class Solution:
    def minimumPushes(self, word: str) -> int:

        count = defaultdict(int)
        for i in word:
            count[i] += 1

        letters = [0 for i in range(26)]
        many = 0

        key = 2
        times = 1
        for i in sorted(count.items(), key= lambda x: x[1], reverse= True):

            idx = ord(i[0])-97
            letters[idx] = (key, times, i[1])
            key += 1

            if key > 9:
                key = 2
                times += 1

        for i in letters:
            if i != 0:
                many += i[1] * i[2]

        return many
