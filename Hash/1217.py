class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        if not position:
            return 0
        odd_cnt,even_cnt = 0,0
        for pos in position:
            if pos % 2 == 0 :
                even_cnt += 1
            else:
                odd_cnt += 1
        if odd_cnt == 0 or even_cnt == 0:
            return 0
        if odd_cnt > even_cnt:
            return even_cnt
        return odd_cnt
