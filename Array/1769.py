class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = []
        for i in range(n):
            cnt = 0
            for j in range(n):
                if j == i:
                    continue
                if boxes[j] == "1":
                    
                    cnt += abs(i-j)
            ans.append(cnt)
        return ans
