# Problem: Long Pressed Name - https://leetcode.com/problems/long-pressed-name/

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:

        if name[0]!=typed[0]: 
            return False

        j=1
        for i in range(1,len(typed)):

            if j<len(name) and typed[i]==name[j]: 
                j+=1
            elif typed[i]!=typed[i-1]: 
                return False

        return j==len(name)