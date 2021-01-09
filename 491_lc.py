class Solution:
    def findSubsequences(self, nums):

        if len(nums) <= 1:
            return []

        self.ans = []


        def backtrack(nums,start,end,res,length):
            if res not in self.ans and len(res) >= length:
                self.ans.append(res[:])

            for i in range(start,end):
                if not res or nums[i] >= res[-1]:
                    res.append(nums[i])
                    backtrack(nums,i+1,end,res,length)

                    res.pop()


        #for j in range(2,len(nums)+1):
        backtrack(nums,0,len(nums),[],2)

        return self.ans
