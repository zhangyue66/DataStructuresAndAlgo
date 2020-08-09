class Solution:
    def reconstructQueue(self, people):
        result = []
        # [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
        # target -> [[7,0],[7,1],[6,1],[5,0],[5,2],[4,4]]
        # iteration 1:res = [[7,0],[7,1]]
        #[[6,1],[5,0],[5,2],[4,4]]
        #iteration 2: res = [[7,0],[6,1],[7,1]]
        #[[5,0],[5,2],[4,4]]
        #iteration 3: res = [[5,0],[7,0],[5,2],[6,1],[7,1]]
        #[[4,4]]
        #iteration 4: res = [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]

        people_dic = {}
        for p in people:
            h,k = p[0],p[1]
            people_dic.setdefault(h,[])
            people_dic[h].append(k)
            #{7: [0, 1], 4: [4], 5: [0, 2], 6: [1]}

        for h in sorted(people_dic.keys(),reverse=True):
            people_dic[h].sort()
            for k in people_dic[h]:
                result.insert(k,[h,k])


        return result


yz = Solution()
people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
print(yz.reconstructQueue(people))
