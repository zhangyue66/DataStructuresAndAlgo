class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        # L,R<10**6 so at most 20 bits
        def helper(number):
            return bin(number).count("1")
        
        is_prime = [2,3,5,7,11,13,17,19]
        cnt = 0
        for i in range(L,R+1):
            if helper(i) in is_prime:
                cnt += 1
                
        return cnt
