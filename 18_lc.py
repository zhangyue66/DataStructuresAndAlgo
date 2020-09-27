class Solution:
    def fourSum(self, nums, target: int):
        ans = []
        nums.sort()
        # dict ={}
        # for num in nums:
        #     if num not in dict:
        #         dict[num] = 1
        #     else:
        #         dict[num] += 1
        #print(nums)
        for i in range(len(nums)-3):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,len(nums)-2):
                if j != i+1 and nums[j] == nums[j-1]:
                    continue

                left,right = j+1,len(nums)-1
                visited = []

                while left < right:

                    if target - nums[i]-nums[j] > nums[left]+nums[right]:
                        left+=1
                    elif target - nums[i]-nums[j] < nums[left]+nums[right]:
                        right-=1
                    else:   #find it
                        if [nums[left],nums[right]] not in visited:
                            ans.append([nums[i],nums[j],nums[left],nums[right]])
                            visited.append([nums[left],nums[right]])

                        left +=1
                        right -=1


        return ans



yz = Solution()
nums =[-1,0,-5,-2,-2,-4,0,1,-2]
target = -9
print(yz.fourSum(nums,target))
