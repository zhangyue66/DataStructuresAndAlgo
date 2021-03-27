class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        ans = []
        
        dict_B = {}
        
        for b in B:
            dict_temp = {}
            for char in b:
                if char not in dict_temp:
                    dict_temp[char] = 1
                else:
                    dict_temp[char] += 1
                    
            for key in dict_temp.keys():
                if key not in dict_B:
                    dict_B[key] = dict_temp[key]
                else:
                    dict_B[key] = max(dict_B[key],dict_temp[key])
                    
        for a in A:
            dict_A = collections.Counter(a)
            found = True
            
            for key in dict_B.keys():
                if key not in dict_A:
                    found = False
                    break
                elif dict_B[key] > dict_A[key]:
                    found = False 
                    break
                    
            if found:
                ans.append(a)
                
                
        return ans
