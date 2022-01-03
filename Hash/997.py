class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust and n == 1:
            return 1
        graph = defaultdict(list)
        judge = set()
        graph_trust =defaultdict(list)
        for tr in trust:
            graph[tr[1]].append(tr[0])
            judge.add(tr[1])
            graph_trust[tr[0]].append(tr[1])
        if not judge:
            return -1
        for j in judge:
            if len(graph[j]) == n-1 and not graph_trust[j]:
                return j
        return -1
            
