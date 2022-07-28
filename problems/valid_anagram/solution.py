class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        
        if(len(s)!=len(t)):
            return False
        
        for i,j in zip(s,t):    
            
            if(d.get(i,None) is not None):
                d[i]+=1
                if(d[i] == 0):
                    d.pop(i)
            else:
                d[i] = 1
            
            if(d.get(j,None) is not None):
                d[j] -= 1
                if(d[j] == 0):
                    d.pop(j)
            else:
                d[j] = -1
            
            
            
            # print(d)
        if(d):
            return False
        else:
            return True
            
        