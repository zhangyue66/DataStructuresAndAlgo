class Solution:
    def characterReplacement(self, s: str, k: int):
        dict ={}
        n = len(s)

        start = 0
        max_len = 0
        max_cnt = 0

        for end in range(n):
            if s[end] not in dict:
                dict[s[end]] = 1
            else:
                dict[s[end]] += 1
            max_cnt = max(max_cnt,dict[s[end]])
            if end-start+1-max_cnt > k:
                dict[s[start]] -= 1
                start += 1

            max_len = max(max_len,end-start+1)

        return max_len
