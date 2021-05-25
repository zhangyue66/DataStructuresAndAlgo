class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def backtrack(target,comb_sum,start,end):
            if target == 0:
                ans.append(comb_sum[:])
                return
            
            for i in range(start,end):
                if target < candidates[i]:
                    break
                comb_sum.append(candidates[i])
                backtrack(target-candidates[i],comb_sum,i,end)
                comb_sum.pop()
                
                
        backtrack(target,[],0,len(candidates))
        
        return ans
