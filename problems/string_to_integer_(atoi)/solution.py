class Solution:
    def myAtoi(self, s: str) -> int:
        nega = False
        x = ''
        
        s = s.strip()
        if(s == ""):
            return 0
        
        if(s[0] not in '-+1234567890'):
            return 0
        
        if(s[0] == '-'):
            nega = True
        
        start = True
        
        for i in s:
            if(i.isdigit()):
                x+=i
                start = False
            if(not i.isdigit()):
                if(not start):
                    break
                if(start):
                    print(i)
                    start = False
        try:
            x = int(x)
        except:
            x = 0
        x = -x if nega else x
        return min((max((x,-2**31)),2**31-1))