class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1 = "yz"
        cnt1 = 0
        cand2 = "yz"
        cnt2 = 0
        
        for num in nums:
            if num == cand1:
                cnt1 += 1
            elif num == cand2:
                cnt2 += 1
            elif cnt1 == 0:
                cand1 = num
                cnt1 += 1
            elif cnt2 == 0:
                cand2 = num
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
                
        # check if candidate 1 and 2 are real majority
        #print(cand1,cand2)
        #print(cnt1,cnt2)
        ans = []
        
        if nums.count(cand1)>len(nums)/3:
            ans.append(cand1)
        if nums.count(cand2) > len(nums)/3:
            ans.append(cand2)
            
        return ans
            
