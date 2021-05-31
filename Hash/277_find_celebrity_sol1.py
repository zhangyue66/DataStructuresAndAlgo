# Suppose you are at a party with n people (labeled from 0 to n - 1), and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know him/her, but he/she does not know any of them.

# Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information about whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

# You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int findCelebrity(n). There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.

 

# Example 1:

# Input: graph = [[1,1,0],[0,1,0],[1,1,1]]
# Output: 1
# Explanation: There are three persons labeled with 0, 1 and 2. graph[i][j] = 1 means person i knows person j, otherwise graph[i][j] = 0 means person i does not know person j. The celebrity is the person labeled as 1 because both 0 and 2 know him but 1 does not know anybody.

# Example 2:

# Input: graph = [[1,0,1],[1,1,0],[0,1,1]]
# Output: -1
# Explanation: There is no celebrity.




# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        not_cele = set()
        
        for a in range(n):
            for b in range(n):
                if a == b:
                    continue
                if b in not_cele:
                    continue
                if knows(a,b):
                    not_cele.add(a)
                else:
                    not_cele.add(b)
                    
                    
        if len(not_cele) == n:
            return -1
        
        cele_candidates = []
        
        for i in range(n):
            if i not in not_cele:
                cele_candidates.append(i)
                
        final = []      
        for cand in cele_candidates:
            is_cele = True
            for p in range(n):
                if cand == p:
                    continue
                if knows(cand,p):
                    is_cele = False
                    break
            if is_cele:
                final.append(cand)
        #print(not_cele,cele_candidates,final)
        if len(final) == 1:
            return final[0]
        return -1
            
        
