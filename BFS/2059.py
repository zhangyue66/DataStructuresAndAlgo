class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        visited = set()
        queue = [(start,0)]
        visited.add(start)
        while queue:
            cur,cnt = queue.pop(0)
            if cur == goal:
                return cnt
            temp = cur
            if 0<=cur<=1000:
                for op in range(3):
                    for num in nums:

                        if op == 0: #add
                            cur += num
                        elif op == 1: # minus
                            cur -= num
                        else: #bitwise xor
                            cur ^= num

                        if  cur not in visited:
                            visited.add(cur)
                            queue.append((cur,cnt+1))
                        cur = temp

        return -1
