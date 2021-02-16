class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        count = []
        for i in range(len(mat)):
            count.append((i,mat[i].count(1)))
            
        count = sorted(count,key = lambda attr:attr[1])
        ans = []
        while k != 0:
            index,cnt = count.pop(0)
            ans.append(index)
            k -=1
            
        return ans
