from collections import Counter
class Solution:
    def customSortString(self, order: str, str: str) -> str:
        str_dict = Counter(str)
        ans = ""
        for char in order:
            if char in str_dict:
                ans += (str_dict[char]*char)
                del str_dict[char]
        for k,v in str_dict.items():
            ans += (k*v)
            
        return ans
