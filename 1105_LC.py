class Solution:
    def minHeightShelves(self, books, shelf_width: int):
        n = len(books)
        res = [float("inf")]*(n+1)
        res[0] = 0 # 0 book height is zero

        for i in range(1,n+1):
            width,height = 0,0
            for j in range(i-1,-1,-1):

                if width + books[j][0] <= shelf_width:
                    height = max(height,books[j][1])
                    width += books[j][0]
                    res[i] = min(res[i],res[j]+height)
                else:
                    break # dont forget this line. When shelf_width is met, need to break.

        return res[n]

yz = Solution()
books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]
shelf_width = 4
print(yz.minHeightShelves(books,shelf_width))
