class Solution(object):
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        cum_shifts = [0]*len(shifts)
        summ = 0
        for i in range(len(shifts)-1, -1, -1):
            summ = (summ + shifts[i]) % 26
            cum_shifts[i] = summ

        alpha_list = list(S)
        for i in range(len(S)):
            tmp = ord(alpha_list[i])+cum_shifts[i]
            if tmp > ord('z'):
                tmp -= ord('z')+1-ord('a')
            alpha_list[i] = chr(tmp)
        return "".join(alpha_list)

yz = Solution()
S = "ruu"
shifts = [26,9,17]
print(yz.shiftingLetters(S,shifts))
