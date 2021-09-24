class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        n = len(palindrome)
        if "a" * n == palindrome:
            return "a" * (n-1) + "b"
        ans,skip = "",False
        if n % 2 == 0:
            # even length. just change first non "a" to "a"
            for i in range(n):
                if palindrome[i] != "a" and not skip:
                    ans += "a"
                    skip = True
                else:
                    ans += palindrome[i]
        else:
            # odd length. make sure first non "a" is not in middle
            mid = n // 2
            for i in range(n):
                if palindrome[i] != "a" and i != mid and not skip:
                    ans += "a"
                    skip = True
                else:
                    if i == n-1 and not skip and palindrome[i] == "a":
                        ans += "b"
                    else:
                        ans += palindrome[i]
        return ans
