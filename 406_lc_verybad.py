class Solution:
    def reconstructQueue(self, people):
        ans = ["yz"]*len(people)
        height = []
        for _ in people:
            if _[0] not in height:
                height.append(_[0])
        height.sort()
        while height:
            cur = height.pop(0)
            yz = []
            for _ in people:
                if _[0] == cur:
                    yz.append(_)

            for node in yz:
                index = node[1]
                cnt = 0
                for i in range(len(ans)):
                    if ans[i] == "yz":
                        if cnt == index:
                            ans[i] = node
                            break
                        elif cnt != index:
                            cnt+=1

                    else:
                        if ans[i][0] >= node[0]:
                            cnt += 1
        #expect            [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
        #1st wrong answer [[5, 0], [7, 0], [6, 1], [5, 2], [4, 4], 'yz']
        return ans

yz = Solution()
people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
print(yz.reconstructQueue(people))
