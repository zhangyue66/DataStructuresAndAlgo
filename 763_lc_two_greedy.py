class Solution:
    def partitionLabels(self, S):
        hash = {l:c for c,l in enumerate(S)}  # rightmost index of each letter

        left,right = 0,0

        res = []

        for i,letter in enumerate(S):
            right = max(right,hash[letter])

            if i == right:
                res.append(right-left+1)
                left = i+1


        return res

yz = Solution()
S = "ababcbacadefegdehijhklij"
print(yz.partitionLabels(S))
