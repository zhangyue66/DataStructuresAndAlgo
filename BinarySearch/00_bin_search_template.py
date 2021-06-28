# [l,r)
#binary search视频 解释开闭区间 https://www.youtube.com/watch?v=J-IQxfYRTto&list=PLLuMmzMTgVK5Hy1qcWYZcd7wVQQ1v0AjX&index=5

# search value
def bin_sec_l(nums,target):
    # [l,r)
    l,r = 0,len(nums)
    while l < r:
        mid = l + (r-l)//2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            r = mid
        else:
            l = mid + 1
    return -1 # not found -1 or l
  
  
# lower_bound - first index of i such that nums[i] >= target
def lower_bound(nums,target):
  l,r = 0,len(nums)
  while l < r:
      mid = l + (r-l)//2
      if nums[mid] >= target:
          r = mid
      else:
          l = mid + 1
  return l

# upper_bound - first index of i such that nums[i] > target
def lower_bound(nums,target):
  l,r = 0,len(nums)
  while l < r:
      mid = l + (r-l)//2
      if nums[mid] > target:
          r = mid
      else:
          l = mid + 1
  return l
