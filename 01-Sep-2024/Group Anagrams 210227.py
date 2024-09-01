# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs):
        groups = defaultdict(list)

        for strng in strs:
            word ="".join(sorted(strng))
            groups[word].append(strng)


        anagrams = []
        for group in groups.values():
            anagrams.append(group)


        return anagrams
