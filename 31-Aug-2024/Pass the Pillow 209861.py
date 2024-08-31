# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:

        person = 1
        last_person = -n

        while time != 0:

            if person == n:
                person = last_person

            elif person == -1:
                person = 1

            time -= 1
            person += 1

        
        if person < 0:
            person = -person

        return person



