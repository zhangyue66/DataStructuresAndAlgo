from collections import defaultdict

class Solution:
    def equationsPossible(self, equations):

        #union_find
        self.graph = defaultdict(list)
        self.parent = [i for i in range(26)]
        for eq in equations:
            if eq[1] == "=":
                self.graph[ord(eq[0])-ord("a")].append(ord(eq[3])-ord("a"))
                self.graph[ord(eq[3])-ord("a")].append(ord(eq[0])-ord("a"))
        def find(a):
            if self.parent[a] == a:
                return a
            return find(self.parent[a])

        def union(a,b):
            pa = find(a)
            pb = find(b)
            if pa != pb :
                self.parent[pa] = pb

        #return self.graph
        #print(self.parent)
        for key,value in self.graph.items():
            #print(key,value)
            if len(value) != 0:
                for node in value:
                    #if find(key) != find(node):
                    union(key,node)

        for e in equations:
            if e[1] == "!":
                if find(ord(e[0])-ord("a")) == find(ord(e[3])-ord("a")):
                    return False

        return True






yz = Solution()
equations = ["a==b","b!=a"]
print(yz.equationsPossible(equations))
