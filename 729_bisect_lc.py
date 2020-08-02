import bisect

class MyCalendar:

    def __init__(self):
        self.calender = []

    def book(self, start: int, end: int) -> bool:
        event = [start,end]
        event_index = bisect.bisect_left(self.calender,event)
        is_left_valid = False
        if event_index == 0 or self.calender[event_index-1][1] <= start:
            is_left_valid = True
        is_right_valid = False
        if event_index == len(self.calender) or self.calender[event_index][0] >= end:
            is_right_valid = True

        if is_left_valid and is_right_valid:
            self.calender.insert(event_index,event)
            return True
        return False
