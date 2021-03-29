class Solution:
    def originalDigits(self, s: str) -> str:
        # 0 : zero   z 
        # 1 : one
        # 2 : two    w
        # 3 : three
        # 4 : four   u
        # 5 : five   
        # 6 : six    x
        # 7 : seven  
        # 8 : eight  g
        # 9 : nine   
        
        ans = ""
        nums = []
        
        dict_str = collections.Counter(s)
        cnt_dict = {}
        
        if "z" in dict_str:
            nums.append(0)
            cnt = dict_str["z"]
            cnt_dict[0] = cnt
            dict_str["e"] = dict_str["e"]-cnt
            dict_str["r"] = dict_str["r"]-cnt
            dict_str["o"] = dict_str["o"]-cnt
            
        if "w" in dict_str:
            nums.append(2)
            cnt = dict_str["w"]
            cnt_dict[2] = cnt
            dict_str["t"] = dict_str["t"]-cnt
            dict_str["o"] = dict_str["o"]-cnt
            
            
        if "u" in dict_str:
            nums.append(4)
            cnt = dict_str["u"]
            cnt_dict[4] = cnt
            dict_str["f"] = dict_str["f"]-cnt
            dict_str["o"] = dict_str["o"]-cnt
            dict_str["r"] = dict_str["r"]-cnt
            
            
        if "x" in dict_str:
            nums.append(6)
            cnt = dict_str["x"]
            cnt_dict[6] = cnt
            dict_str["s"] = dict_str["s"]-cnt
            dict_str["i"] = dict_str["i"]-cnt
        
        if "g" in dict_str:
            nums.append(8)
            cnt = dict_str["g"]
            cnt_dict[8] = cnt
            dict_str["e"] = dict_str["e"]-cnt
            dict_str["i"] = dict_str["i"]-cnt
            dict_str["h"] = dict_str["h"]-cnt
            dict_str["t"] = dict_str["t"]-cnt
            
        if "o" in dict_str and dict_str["o"] != 0:
            # there is one
            nums.append(1)
            cnt = dict_str["o"]
            cnt_dict[1] = cnt
            dict_str["n"] = dict_str["n"] - cnt
            dict_str["e"] = dict_str["e"] - cnt
            
            
        if "t" in dict_str and dict_str["t"] != 0:
            # there is 3 existing
            nums.append(3)
            cnt = dict_str["t"]
            cnt_dict[3] = cnt
            dict_str["h"] = dict_str["h"] - cnt
            dict_str["r"] = dict_str["r"] - cnt
            dict_str["e"] = dict_str["e"] - cnt
            dict_str["e"] = dict_str["e"] - cnt
            
        if "f" in dict_str and dict_str["f"] != 0:
            # there is 5 existing
            nums.append(5)
            cnt = dict_str["f"]
            cnt_dict[5] = cnt
            dict_str["i"] = dict_str["i"] - cnt
            dict_str["v"] = dict_str["v"] - cnt
            dict_str["e"] = dict_str["e"] - cnt
            
        if "s" in dict_str and dict_str["s"] != 0:
            # there is 7 existing
            nums.append(7)
            cnt = dict_str["s"]
            cnt_dict[7] = cnt
            dict_str["e"] = dict_str["e"] - cnt
            dict_str["v"] = dict_str["v"] - cnt
            dict_str["e"] = dict_str["e"] - cnt
            dict_str["n"] = dict_str["n"] - cnt
            
        if "i" in dict_str and dict_str["i"] != 0:
            # there is 9 existing
            nums.append(9)
            cnt = dict_str["i"]
            cnt_dict[9] = cnt
            dict_str["n"] = dict_str["n"] - cnt
            dict_str["n"] = dict_str["n"] - cnt
            dict_str["e"] = dict_str["e"] - cnt
        
        
        nums.sort()
        
        for num in nums:
            ans += str(num)*cnt_dict[num]
        
        return ans
            
            
            
