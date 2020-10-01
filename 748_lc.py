class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        dict = {}
        for letter in licensePlate:
            if letter.isalpha():
                if letter.lower() not in dict:
                    dict[letter.lower()] = 1
                    
                else:
                    dict[letter.lower()] += 1
                    
                    
        #{"s":2,"p":1,"t":1}
        lp_list = list(dict.keys())
        res = []
        for word in words:
            match = 1
            for key in lp_list:
                if word.count(key) < dict[key]:
                    match =0
                    break
                    
            if match == 0:
                match = 1
                continue
            else:
                res.append(word)
                
        if len(res) ==1:
            return res[0]
        else:
            min_len = float("inf")
            for ans in res:
                min_len = min(len(ans),min_len)
                
            for ans in res:
                if len(ans) == min_len:
                    return ans
                
            
            
