class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        neg = ((dividend<0) != (divisor <0))
        
        res = 0
        dividend,divisor = abs(dividend),abs(divisor)
        
        while dividend >= divisor:
            temp = divisor
            multi = 1
            
            while dividend >= temp :
                dividend -= temp
                res += multi
                multi <<= 1
                temp <<= 1
                
        #print(neg)   
        if neg:
            return max(-res,(-2)**31)
        else:
            return min(res,2**31-1)
        
