import bisect
class MyCalendar:

    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:
        #using binary search
        event = (start,end)
        if not self.events:
            self.events.append(event)
            return True 
        target_index = bisect.bisect_left(self.events,event)
        #print(target_index)
        is_leftvalid,is_rightvalid = False,False
        if target_index == 0:
            is_leftvalid = True
            if event[1] <= self.events[0][0]:
                is_rightvalid = True
        elif target_index == len(self.events) :
            is_rightvalid = True
            if event[0] >= self.events[-1][1]:
                is_leftvalid = True
        else:
            if start >= self.events[target_index-1][1]:
                is_leftvalid = True
            if end <= self.events[target_index][0]:
                is_rightvalid = True
                
        if is_leftvalid and is_rightvalid:
            self.events.insert(target_index,event)
            return True
        return False
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
