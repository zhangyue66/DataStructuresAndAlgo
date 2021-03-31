class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if len(envelopes) == 1:
            return 1
        envelopes.sort(key=lambda x:x[0])       
        #print(envelopes)
        cnts =[1]*len(envelopes)
        
        max_len = 0
        for i in range(1,len(envelopes)):
            for j in range(i):
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    cnts[i] = max(cnts[i],cnts[j]+1)
            max_len = max(max_len,cnts[i])
        return max_len
                    
                
