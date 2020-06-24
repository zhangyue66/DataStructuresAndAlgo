class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str):
        if len(croakOfFrogs) == 0 or len(croakOfFrogs)%5 !=0:
            return -1
        else:
            dict = {}
            for _ in croakOfFrogs:
                if _ not in dict:
                    dict[_] = 1
                else:
                    dict[_] += 1
            ans = dict["c"]
            for key,value in dict.items():
                if value != ans:
                    return -1

            c,r,o,a,k = 0,0,0,0,0
            frog = 0
            res = 0

            for ch in croakOfFrogs:
                if ch == "c":
                    c += 1
                    frog += 1
                elif ch == "r":
                    r += 1
                elif ch == "o":
                    o+=1
                elif ch == "a":
                    a += 1
                elif ch == "k":
                    k += 1
                    frog -= 1

                res = max(res,frog)

                if frog >= 0 and (c >= r and r >= o and o >= a and a >=k ):
                    continue
                else:
                    return -1


            return res

yz = Solution()
croakOfFrogs = "croakcroak"
print(yz.minNumberOfFrogs(croakOfFrogs))
