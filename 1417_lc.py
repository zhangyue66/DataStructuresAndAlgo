class Solution:
    def reformat(self, s: str) -> str:
        alpha_cnt,number_cnt = 0,0
        alpha_li,num_li = [],[]
        ans = ""
        
        for a in s:
            #print(a,a.isnumeric(),alpha_cnt,number_cnt)
            if a.isnumeric() == True:
                number_cnt += 1
                num_li.append(a)
            else:
                alpha_cnt += 1
                alpha_li.append(a)
                
        #print(alpha_li,num_li)
        
        if abs(alpha_cnt-number_cnt) > 1:
            return ""
        else:
            
            if alpha_cnt > number_cnt:
                while number_cnt > 0:
                    ans += (alpha_li[number_cnt-1]+num_li[number_cnt-1])
                    number_cnt -= 1
                
                ans += alpha_li[-1]
            elif number_cnt > alpha_cnt:
                while alpha_cnt > 0:
                    ans += (num_li[alpha_cnt-1]+alpha_li[alpha_cnt-1])
                    alpha_cnt -= 1
                ans += num_li[-1]
            else:
                while number_cnt > 0:
                    ans += (alpha_li[number_cnt-1]+num_li[number_cnt-1])
                    number_cnt -= 1
                  
            return ans
                
        
        
        
        
