class Solution:
    def minimumLengthEncoding(self, words):
        res = ""

        done = []
        words = [x[::-1] for x in words]
        words.sort()
        #['em', 'emit', 'lleb']
        for i in range(len(words)):
            if i < len(words)-1 and words[i+1].find(words[i]) == 0:
                continue
            else:
                res += (words[i][::-1]+"#")

        return len(res)
        
        
        
words = ["time", "me", "bell"]
yz = Solution()
print(yz.minimumLengthEncoding(words))
