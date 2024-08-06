# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs):

        sorted_w = defaultdict(list)

        for word in strs:
            curr = ''.join(sorted(word))
            sorted_w[curr].append(word)

        answer = []
        for i,groups in sorted_w.items():
            answer.append(groups)

        return answer