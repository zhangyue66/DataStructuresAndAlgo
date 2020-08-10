class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) ==0:
            return []
        dict = {}
        for i in range(len(nums)):
            dict[nums[i]] = i
            
        print(dict)
        
        for i in range(len(nums)):
            target_value = target - nums[i]
            if target_value in dict:
                if dict[target_value] != i:
                    return [i,dict[target_value]]
        return []
