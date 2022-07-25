class Solution:
    def isHappy(self, n: int) -> bool:
        
        s = set()
        while n!=1:
            n = sum(map( lambda x: int(x)**2, list(str(n))))
            if(n in s):
                return False
            s.add(n)
        return True
            