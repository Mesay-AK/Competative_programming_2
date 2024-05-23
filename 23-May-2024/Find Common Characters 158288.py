# Problem: Find Common Characters - https://leetcode.com/problems/find-common-characters/

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        dictionary=dict()
        result=[]
        for char in words[0]:
            if char not in dictionary:
                dictionary[char] = [1]

            else:
                dictionary[char][0] += 1

        for i in range(1,len(words)):
            for char in words[i]:
                if char in dictionary.keys():
                    if len(dictionary[char]) == i:
                        dictionary[char].append(1)

                    else:
                        dictionary[char][-1] += 1

        for key in dictionary.keys():
            if len(dictionary[key]) == len(words):
                temp = key*min(dictionary[key])
                temp.split()
                result += temp
        return result