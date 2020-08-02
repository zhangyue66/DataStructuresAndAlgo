class MyCalendar:

    def __init__(self):
        self.calender = []

    def book(self, start: int, end: int) -> bool:
        for s,e in self.calender:
            
            if e > start and s < end:
                return False
        self.calender.append((start,end))
            
        return True
        
