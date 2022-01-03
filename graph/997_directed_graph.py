class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # directed graph - indegree and outdegree
        indegrees = [0]*(n+1)
        outdegrees = [0]*(n+1)
        for tr in trust:
            outdegrees[tr[0]] += 1
            indegrees[tr[1]] += 1
        for people in range(1,n+1):
            if indegrees[people] - outdegrees[people] == n - 1:
                return people
        return -1
