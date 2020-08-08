class MyCalendarTwo:

    def __init__(self):
        self.calender = []
        self.overlap = []
        

    def book(self, start: int, end: int) -> bool:
        event = (start,end)
        
        for s,e in self.overlap:
            if max(start,s) < min(end,e):
                return False
        for s,e in self.calender:
            ss = max(start,s)
            ee = min(end,e)
            if ss < ee : # means there is intersection
                self.overlap.append((ss,ee))
                
        self.calender.append(event)
        
        return True
