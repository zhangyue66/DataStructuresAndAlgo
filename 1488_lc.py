class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        lakes = collections.defaultdict(bool)
        lastrain = collections.defaultdict(int)
        res = []
        dry = []
        for k,v in enumerate(rains):
            if v > 0:
                if not lakes[v]:
                    lakes[v] = True
                    res.append(-1)
                    lastrain[v] = k
                else:
                    # lakes[v] == True
                    if dry == []:
                        return []
                    else:
                        # check if there is a dry day we can use
                        i = 0
                        found = False
                        while i < len(dry) and not found:
                            if dry[i] > lastrain[v]:
                                found = True
                                dry_day = dry[i]
                            else:
                                i += 1
                        if found:
                            res[dry_day] = v
                            lastrain[v] = k
                            dry.pop(i)
                            res.append(-1)
                        else:
                            return []
            elif v == 0:
                res.append(1)
                dry.append(k)
        return res
