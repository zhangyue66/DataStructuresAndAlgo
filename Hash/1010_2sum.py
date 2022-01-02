from collections import defaultdict
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        if len(time) <= 1:
            return 0
        modulo_map = defaultdict(int)
        for t in time:
            mod = t % 60
            modulo_map[mod] += 1
        ans = 0
        for mod,count in modulo_map.items():
            if mod == 0 or mod == 30:
                ans += (count*(count-1))//2
            elif mod < 30:
                target_mod = 60 - mod
                if target_mod in modulo_map:
                    if target_mod == mod and count >= 2:
                        ans += (count*(count-1))//2
                    else:
                        ans += (modulo_map[mod]*modulo_map[target_mod])
        
        return ans
