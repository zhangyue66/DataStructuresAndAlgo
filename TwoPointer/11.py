class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        
        area = min(height[l],height[r])*(r-l)
        
        while l+1 < r:
            #need to check l is shorter or right is shorter
            if height[l] <= height[r]:
                target = l
                while target+1 < r and height[target] <= height[l]:
                    target += 1
                l = target   
                area = max(area,min(height[target],height[r])*(r-target))
            else:
                target = r
                while target > l+1 and height[target] <= height[r]:
                    target -= 1
                    
                r = target
                area = max(area,min(height[l],height[target])*(target-l))
                
                
        return area
