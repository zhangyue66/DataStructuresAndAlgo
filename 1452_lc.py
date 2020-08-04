class Solution:
    def peopleIndexes(self, favoriteCompanies):
        ans = []

        for i in range(len(favoriteCompanies)):
            cnt = 0
            for j in range(len(favoriteCompanies)):
                if i != j and set(favoriteCompanies[i]).issubset(set(favoriteCompanies[j])) == True:
                    cnt += 1
                    continue
            if cnt == 0:
                ans.append(i)

        return ans

yz = Solution()
favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]
#favoriteCompanies = [["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]]
#favoriteCompanies = [["leetcode"],["google"],["facebook"],["amazon"]]
#favoriteCompanies = [["nxaqhyoprhlhvhyojanr","ovqdyfqmlpxapbjwtssm","qmsbphxzmnvflrwyvxlc","udfuxjdxkxwqnqvgjjsp","yawoixzhsdkaaauramvg","zycidpyopumzgdpamnty"],["nxaqhyoprhlhvhyojanr","ovqdyfqmlpxapbjwtssm","udfuxjdxkxwqnqvgjjsp","yawoixzhsdkaaauramvg","zycidpyopumzgdpamnty"],["ovqdyfqmlpxapbjwtssm","qmsbphxzmnvflrwyvxlc","udfuxjdxkxwqnqvgjjsp","yawoixzhsdkaaauramvg","zycidpyopumzgdpamnty"]]

print(yz.peopleIndexes(favoriteCompanies))
