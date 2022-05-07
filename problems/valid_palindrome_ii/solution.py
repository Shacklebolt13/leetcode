class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = len(s)
        c = False
        if(l%2==0):
            for i,j in zip(range(0,l//2,1),range(l-1,l//2 -1,-1)):        
                if(s[i]!=s[j]):  
                    c = (i,j)
                    break
            
        else:
            for i,j in zip(range(0,l//2,1),range(l-1,l//2,-1)):
                if(s[i]!=s[j]):
                    c = (i,j)
                    break
                    
        if(not c):
            return True
        else:
            tmp = s[i]
            s = s[:i]+s[i+1:]
            print(s)
            if(s==s[::-1]):
                return True
            
            s = s[:i]+tmp+s[i:j-1] +s[j:]
            print(s)
            if(s==s[::-1]):
                return True
            return False
            