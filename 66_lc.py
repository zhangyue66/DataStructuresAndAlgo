class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
        
        else:
            carry = True
            n = len(digits) - 1
            
            while carry == True:
                digits[n] = 0
                if n > 0:
                    if digits[n-1] == 9:
                        carry = True
                    else:
                        digits[n-1] += 1
                        carry = False
                    n -= 1
                elif n == 0:
                    digits[0] = 0
                    digits.insert(0,1)
                    carry = False
                    
        
        
        
        return digits
