class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        
        while (b & mask) != 0:
            a = a ^ b
            carry = a & b
            b = carry << 1
        # if b is negative number , b will never be 0 when shifting left.
        if b > 0:
            
            return a & mask
        return a
            
