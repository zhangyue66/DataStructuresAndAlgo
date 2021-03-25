class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        dict = defaultdict(list)
        A_nums = sorted(A)
        B_nums = sorted(B)
        
        rest,ans = [],[]
        
        
        pb = 0 # pointer at B_nums
        
        for a in A_nums:
            if a > B_nums[pb]:
                dict[B_nums[pb]].append(a)
                pb += 1
            else:
                rest.append(a)
                
                
        for b in B:
            if b in dict and dict[b]:
                num = dict[b].pop()
                ans.append(num)
                
            else:
                num = rest.pop()
                ans.append(num)
                
        return ans
                
                
