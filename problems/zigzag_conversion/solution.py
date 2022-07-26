class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows == 1):
            return s
        l = len(s)
        x = 0
        s = list(s)
        d = [""] * numRows
        dec = False
        print(d)
        
        while s:
            d[x]+=s.pop(0)
            
            if(dec):
                x = x-1
                
                if(x == 0):
                    dec = False
            else:
                x = x+1
                
                if(x == numRows-1):
                    dec = True
                
        return "".join(d)
        
        
        
        
        
        
                