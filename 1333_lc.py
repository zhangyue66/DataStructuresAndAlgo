class Solution:
    def filterRestaurants(self, restaurants, veganFriendly: int, maxPrice: int, maxDistance: int):
        candidate = []
        for restaurant in restaurants:
            if veganFriendly == 1:
                if restaurant[2] == veganFriendly  and restaurant[3]<=maxPrice and restaurant[4]<= maxDistance:
                    candidate.append(restaurant)
            else:
                if restaurant[3]<=maxPrice and restaurant[4] <= maxDistance:
                    candidate.append(restaurant)

        if len(candidate) == 0:
            return []
        else:
            #print(candidate)
            candidate.sort(key= lambda i : (i[1],i[0]),reverse=True )

            res = []
            for _ in candidate:
                res.append(_[0])

            return res
yz = Solution()
restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]]
veganFriendly = 1
maxPrice = 50
maxDistance = 10
print(yz.filterRestaurants(restaurants,veganFriendly,maxPrice,maxDistance))
