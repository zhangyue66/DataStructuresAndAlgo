class Solution:
    def arrangeWords(self, text):
        words = text.split(" ")
        replace = ""
        for s in words[0]:
            if s.isupper():
                s = s.lower()

            replace += s

        words[0] = replace # here finish the first capital transition

        # wordss = []
        #
        # for i in range(len(words)):
        #     input = []
        #     input.append(words[i])
        #     input.append(i)
        #     wordss.append(input)

        #return wordss #[['leetcode', 0], ['is', 1], ['cool', 2]]
        #word,position

        #ans = []

        ans = sorted(words,key=len)

        cap = ""

        for i in range(len(ans[0])):
            if i ==0:
                yz = ans[0][i].upper()
            else:
                yz = ans[0][i]

            cap += yz

        ans[0] = cap
        return " ".join(ans)



yz = Solution()
text = "Leetcode is cool"
print(yz.arrangeWords(text))
