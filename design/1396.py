class UndergroundSystem:

    def __init__(self):
        self.hash_checkin = {} #save id as key, value is tuple(station,time)
        self.hash_total = {} # save [startStation,endStation] as key, value is tuple(total_time,count)
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.hash_checkin[id] = (stationName,t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation,startTime = self.hash_checkin[id]
        if (startStation,stationName) not in self.hash_total:
            self.hash_total[(startStation,stationName)] = (t-startTime,1)
            
        else:
            time,cnt = self.hash_total[(startStation,stationName)]
            
            self.hash_total[(startStation,stationName)] = (time+t-startTime,cnt+1)
            #del self.hash_checkin[(startStation,startTime)]
        
         

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        time,cnt = self.hash_total[(startStation,endStation)]
        return time/cnt


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
