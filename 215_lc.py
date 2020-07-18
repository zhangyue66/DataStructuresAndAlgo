class Solution:
    def findKthLargest(self, nums, k: int):
        if len(nums) == 0:
            return None

        else:

            dict = {}
            bucket =[]

            for num in nums:
                if num not in dict:
                    bucket.append(num)
                    dict[num] = 1
                else:
                    dict[num] += 1


            bucket.sort(reverse=True)

            cnt = 0
            i = 0

            while cnt < k:

                cnt += dict[bucket[i]]

                if cnt >= k:
                    break
                else:
                    i+=1


            return bucket[i]


yz = Solution()
nums,k = [3,2,3,1,2,4,5,5,6], 4
print(yz.findKthLargest(nums,k))
