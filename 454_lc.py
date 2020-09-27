class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        cnt = 0
        dic = {}
        for a in A:
            for b in B:
                if a+b not in dic:
                    dic[a+b] = 1
                else:
                    dic[a+b] += 1
                    
                    
        for c in C:
            for d in D:
                if -c-d in dic:
                    cnt += dic[-c-d]
                    
        return cnt
