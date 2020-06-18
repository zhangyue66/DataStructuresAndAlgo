class Solution:
    def combine(self, n: int, k):
        if k > n :
            return []
        else:
            res = []

            def helper(n,k,res,path,index):
                if k == 0:
                    res.append(path)
                    return
                else:
                    for i in range(index,n+1):
                        helper(n,k-1,res,path+[i],i+1)


            helper(n,k,res,[],1)

            return res
