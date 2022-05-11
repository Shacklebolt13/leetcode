class Solution:
    def convs(self,r):
        if(r=='I'):
            return 1
        if(r=='V'):
            return 5
        if(r=='X'):
            return 10
        if(r=='L'):
            return 50
        if(r=='C'):
            return 100
        if(r=='D'):
            return 500
        if(r=='M'):
            return 1000

    
    def romanToInt(self, s: str) -> int:
        l = len(s)
        res = 0
        i=0
        while i<l:
            v1 = self.convs(s[i])
            if((i+1) < l):
                v2 = self.convs(s[i+1])
                
                if(v1>=v2):
                    print(v1)
                    res+=v1
                    i+=1
                else:
                    print(v2,'-',v1)
                    res += v2-v1
                    i+=2
            else:
                print(v1)
                res+=v1
                i+=1
            
            
        return res