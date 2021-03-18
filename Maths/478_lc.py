class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.R = radius
        self.x_center = x_center
        self.y_center = y_center
        self.x_range = [self.x_center-self.R,self.x_center+self.R]
        self.y_range = [self.y_center-self.R,self.y_center+self.R]

    def randPoint(self) -> List[float]:
        #self.ans = []
        stop = False
        
        while not stop:
            x= random.uniform(self.x_range[0],self.x_range[1])
            y = random.uniform(self.y_range[0],self.y_range[1])
            
            if ((x-self.x_center)**2 + (y-self.y_center)**2)**0.5 <= self.R:
                stop = True
                
        return [x,y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
