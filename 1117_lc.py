class Solution:
    def canMakePaliQueries(self, s: str, queries):
        ans = []


        cnt = [[0] * 26]


        for i,c in enumerate(s):
            cnt.append(cnt[i][:])

            cnt[i+1][ord(c)-ord("a")] += 1

        #return cnt  -> number of character is cnt[i+1]-cnt[i]

        for left,right,number in queries:
            list_r = cnt[right+1]
            list_l = cnt[left]
            counter = 0
            for i in range(26):
                number_cnt = list_r[i] - list_l[i]
                if number_cnt % 2 != 0 : # if number appears in pairs we dont need to worry
                    counter += (number_cnt%2)
            #print(counter)
            if counter//2 <= number:
                ans.append(True)
            else:
                ans.append(False)

        return ans
