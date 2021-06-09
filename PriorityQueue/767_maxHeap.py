from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        # use heap , if heappop poping an element which is same as prev , return ""
        ans = ""
        maps = Counter(s)
        heap = []
        for key,value in maps.items():
            heapq.heappush(heap,(-value,key))
        prev_char = None 
        prev_freq = 0
        
        while len(heap) > 0 :
            
            freq,char = heapq.heappop(heap)
            ans += char
            freq += 1 # because max heap
            if prev_freq < 0:
                heapq.heappush(heap,(prev_freq,prev_char))
            prev_freq,prev_char = freq,char
            
        if len(ans) != len(s):
            return ""
        return ans
            
