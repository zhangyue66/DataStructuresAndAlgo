class Solution:
    def minDominoRotations(self, A, B):
        ans = float("inf")

        # element which can make the change must at least have len(a) as count . so ideally we at most have 2 elements that can be candidate

        n = len(A)

        candidates = []

        hash = {}

        for i in range(n):
            if A[i] not in hash:
                hash[A[i]] = 1
            else:
                hash[A[i]] += 1

            if B[i] not in hash:
                hash[B[i]] = 1
            else:
                hash[B[i]] += 1
        #print(hash)
        for k,v in hash.items():
            if v >= n :
                candidates.append(k)
        #print(candidates)
        if len(candidates) == 0:
            return -1
        #print(ans)
        for cand in candidates:

            for i in range(n):

                if A[i] != cand and B[i] != cand:
                    return -1

            cnt1 = n-A.count(cand)
            cnt2 = n-B.count(cand)

            ans = min(ans,min(cnt1,cnt2))

        return ans


yz = Solution()
A = [2,1,2,4,2,2]
B = [5,2,6,2,3,2]
print(yz.minDominoRotations(A,B))
