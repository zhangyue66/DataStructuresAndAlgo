class Solution:
    def makeConnected(self, n: int, connections):
        if len(connections)<n-1:
            return -1

        self.parent = [i for i in range(n)]

        def find(a):
            if self.parent[a] == a:
                return a
            return find(self.parent[a])

        def union(a,b):
            pa = find(a)
            pb = find(b)
            if pa != pb:
                self.parent[pa] = pb

        ans=n-1 # if n nodes all connected, we just need n-1 vertic

        for a,b in connections:
            parent_a = find(a)
            parent_b = find(b)
            if parent_a != parent_b :
                union(a,b)
                ans -= 1
        return ans
