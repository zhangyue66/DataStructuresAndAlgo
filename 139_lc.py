class Solution:
    def wordBreak(self, s: str, wordDict):
        stack = [0]
        seen = set()

        while stack:
            cur = stack.pop()
            if cur in seen:
                continue
            seen.add(cur)

            for word in wordDict:
                if s[cur:].startswith(word):
                    x = len(word)

                    if x == len(s[cur:]):
                        return True
                    stack.append(cur+x)

        return False
