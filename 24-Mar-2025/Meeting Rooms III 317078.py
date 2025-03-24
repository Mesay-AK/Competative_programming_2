# Problem: Meeting Rooms III - https://leetcode.com/problems/meeting-rooms-iii/

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:

        events.sort()
        min_heap = []
        event_index = num_attended = 0
        total_days = max(e[1] for e in events)

        for day in range(1, total_days + 1):
            while event_index < len(events) and events[event_index][0] == day:
                heapq.heappush(min_heap, events[event_index][1])
                event_index += 1

            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)

            if min_heap:
                heapq.heappop(min_heap)
                num_attended += 1

            if event_index == len(events) and not min_heap:
                break

        return num_attended