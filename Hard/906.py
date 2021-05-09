class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        # break down to 10**9 and then 12 + 21 123+21 breaks down to 10**5
        def check_palindrom(number):
            str_number = str(number)
            return str_number == str_number[::-1]
        
        def create_even_palindrom(str):
            return str+str[::-1]
        def create_odd_palindrom(str):
            return str+str[:-1][::-1]

            
        ans = 0
        L,R = int(left),int(right)
        # create palindrom from number range(10**5)
        for i in range(1,10**5+1):
            num_str = create_even_palindrom(str(i))
            if (int(num_str))**2 > R:
                break
            if (int(num_str))**2 >= L:
                if check_palindrom((int(num_str))**2):
                    ans += 1
        for i in range(1,10**5+1):
            num_str = create_odd_palindrom(str(i))
            if (int(num_str))**2 > R:
                continue
            if (int(num_str))**2 >= L:
                if check_palindrom((int(num_str))**2):
                    ans += 1
                    
        return ans
            
        
