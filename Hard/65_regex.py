import re
class Solution:
    def isNumber(self, s: str) -> bool:
        # using regex pattern
        
        # starting with +-
        # decimal number .1 1.1 1. or
        # integer 57678
        pattern = r'^[+-]?((\d+\.?\d*)|(\.\d+)|\d+)([eE][+-]?\d+)?$'
        #pattern = r"^[+-]?((\d+\.?\d*)|(\d*\.?\d+))([eE][+-]?\d+)?$"
        
        return re.match(pattern,s)
        
        
