class Solution:
    def averageWaitingTime(self, customers) :
        wait = 0
        start,end = 0,0

        for customer in customers:
            if customer[0]>= end:
                start = max(customer[0],end)
                end = start+customer[1]

                wait += end - start

            else:
                wait += end - customer[0]
                end = end + customer[1]
                wait += customer[1]

        return wait/len(customers)




yz = Solution()
#customers = [[1,2],[2,5],[4,3]]
customers = [[5,2],[5,4],[10,3],[20,1]]
print(yz.averageWaitingTime(customers))
