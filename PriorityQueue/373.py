import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ans = []
        
        i , j = 0 , 0
        visited = set()
        li = [(nums1[i]+nums2[j],i,j)]
        visited.add((i,j))
        heapq.heapify(li)
        m,n = len(nums1),len(nums2)
        
        while len(ans) < k and li:
            smallest = heapq.heappop(li) # value,index i,index j
            ans.append([nums1[smallest[1]],nums2[smallest[2]]])
            
            if smallest[1] + 1 < m and (smallest[1]+1,smallest[2]) not in visited:
                heapq.heappush(li,(nums1[smallest[1]+1]+nums2[smallest[2]],smallest[1]+1,smallest[2]))
                visited.add((smallest[1]+1,smallest[2]))
            
            if smallest[2] + 1 < n and (smallest[1],smallest[2]+1) not in visited:
                heapq.heappush(li,(nums1[smallest[1]]+nums2[smallest[2]+1],smallest[1],smallest[2]+1))
                visited.add((smallest[1],smallest[2]+1))
                
                
        return ans
            
        
        
            
        
        
