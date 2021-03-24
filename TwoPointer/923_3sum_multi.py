class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        dict = collections.Counter(arr)
        
        ans = 0
        
        for i in dict:
            for j in dict:
                k = target-i-j
                
                if i == j ==k:
                    ans += dict[i]*(dict[i]-1)*(dict[i]-2)//6  # C(cnt,3) ,cnt = dict[i]
                elif i == j:
                    ans += dict[i]*(dict[i]-1)//2*dict[k]
                elif i < j < k:
                    ans += dict[i]*dict[j]*dict[k]
 
                    
        return ans%(10**9+7)
