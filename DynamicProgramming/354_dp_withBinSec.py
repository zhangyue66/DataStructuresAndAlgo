class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        #if width are same, sort the height in descending order
        envelopes.sort(key= lambda x:(x[0],-x[1]))
        #print(envelopes)  [[2, 3], [5, 4], [6, 7], [6, 4]]
        
        dp = [0] * len(envelopes)
        max_len = 0
        
        def bin_search(arr,start,end,target):
            while start < end:
                mid = start + (end-start) //2
                if arr[mid] == target:
                    return mid
                elif arr[mid] > target:
                    end = mid
                else:
                    start = mid + 1
                    
            return start
                
        for i in range(len(envelopes)):
            # find the index of height of envelope[i]
            index = bin_search(dp,0,max_len,envelopes[i][1])
            dp[index] = envelopes[i][1]
            
            if index == max_len:
                max_len += 1
                
        return max_len
        
