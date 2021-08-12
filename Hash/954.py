from collections import Counter
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        mapping = Counter(arr)
        n = len(arr)
        arr.sort()
        for i in range(n):
            if arr[i] < 0:
                if arr[i] in mapping and mapping[arr[i]] == 0:
                    continue
                else:
                    target = arr[i] / 2
                    if target not in mapping:
                        return False
                    if mapping[target] == 0:
                        return False
                    mapping[target] -= 1
                    mapping[arr[i]] -= 1
            if arr[i] >= 0:
                if arr[i] in mapping and mapping[arr[i]] == 0:
                    continue
                else:
                    target = arr[i] * 2
                    if target not in mapping:
                        return False
                    if mapping[target] == 0:
                        return False
                    mapping[target] -= 1
                    mapping[arr[i]] -= 1
        return True
