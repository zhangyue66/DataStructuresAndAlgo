class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = 0
        bin_x = bin(x)[2::]
        bin_y = bin(y)[2::]
        if len(bin_x) != len(bin_y):
            diff = abs(len(bin_y)-len(bin_x))
            if len(bin_y) > len(bin_x):
                bin_x = ("0"*diff+bin_x)
            else:
                bin_y = ("0"*diff+bin_y)
                
        for i in range(len(bin_x)):
            if bin_x[i] != bin_y[i]:
                ans += 1
        return ans
