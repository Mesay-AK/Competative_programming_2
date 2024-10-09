# Problem: My Calendar II - https://leetcode.com/problems/my-calendar-ii/

class MyCalendarTwo:

    def __init__(self):
        self.nonOverlap = []
        self.overlap = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.overlap:
            if end > s and e > start:
                return False

        for s, e in self.nonOverlap:
            if end > s and e > start:
                self.overlap.append((max(s, start), min(e, end)))
        self.nonOverlap.append((start, end))
        
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)