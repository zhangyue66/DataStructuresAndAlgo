class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        press_time = 0
        ans = ""
        #dic = {}
        n = len(releaseTimes)
        for i in range(n):
            if i == 0:
                #dic[keysPressed[i]] = releaseTimes[i]
                press_time = releaseTimes[i]
                ans = keysPressed[i]
            else:
                time = releaseTimes[i] - releaseTimes[i-1]
                if time > press_time:
                    ans = keysPressed[i]
                    press_time = time
                if time == press_time and keysPressed[i] > ans:
                    ans = keysPressed[i]
        return ans
                
