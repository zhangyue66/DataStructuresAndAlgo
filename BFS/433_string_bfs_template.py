class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        # because mutation is random at postion. so we can not check from start . need to BFS all posible solutions
        n = len(start)
        queue = [(start,0)]
        ans = 111 # because max(n) = 8
        visited = set()
        while queue:
            cur_word,mutate_cnt = queue.pop(0)
            if cur_word == end:
                ans = min(ans,mutate_cnt)
            for i in range(n):
                for char in ["A","C","G","T"]:
                    if cur_word[i] == char:
                        continue
                    new_word = cur_word[:i]+char+cur_word[i+1:]
                    if new_word in bank and new_word not in visited:
                        queue.append((new_word,mutate_cnt+1))
                        visited.add(new_word)
        if ans == 111:
            return -1
        return ans
