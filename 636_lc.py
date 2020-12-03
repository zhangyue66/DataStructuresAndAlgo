class Solution:
    def exclusiveTime(self, n: int, logs):

        stack = []

        ans = [0]*n

        # total_time = logs[-1]
        # total_time=total_time.split(":")
        # total_time = int(total_time[2])+1
        # delta = 0
        prev = 0
        for log in logs:
            log = log.split(":")
            #print(log)  # ['0', 'start', '0'] ['1', 'start', '2'] ['1', 'end', '5'] ['0', 'end', '6']

            id = int(log[0])
            action = log[1]
            time = int(log[2])

            if action == "start":
                if len(stack) != 0 :
                    ans[stack[-1]] += time - prev
                stack.append(id)
                prev = time
            else:
                ans[stack.pop()] += time-prev+1
                prev = time+1

        return ans

yz = Solution()
n = 2
logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
print(yz.exclusiveTime(n,logs))
