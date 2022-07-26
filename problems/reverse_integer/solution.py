class Solution:
    def reverse(self, x: int) -> int:
        tmp = 0
        negative = False
        
        if(x<0):
            x = -x
            negative = True
        while x!=0:
            tmp = tmp*10  + x%10
            x//=10
        
        if(negative):
            tmp = -tmp
            
        return tmp if (tmp <= 2**31-1 and tmp>=-2**31) else 0 
        