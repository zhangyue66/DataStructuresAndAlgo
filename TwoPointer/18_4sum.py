class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # O(n^3) method
        ans = []
        n = len(nums)
        if n < 4:
            return []
        nums.sort()
        visited = set()
        for i in range(n-3):
            for j in range(i+1,n-2):
                k,l = j+1,n-1
                while k < l:
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        if (nums[i],nums[j],nums[k],nums[l]) not in visited:
                            ans.append((nums[i],nums[j],nums[k],nums[l]))
                            visited.add((nums[i],nums[j],nums[k],nums[l]))
                        k += 1
                        l -= 1
                    elif nums[i] + nums[j] + nums[k] + nums[l] < target:
                        k += 1
                    else:
                        l -= 1
        return ans
                        
