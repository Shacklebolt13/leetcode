class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(':')',
             '[':']',
             '{':'}',
            }
        
        st = []
        
        for x in s:
            if(d.get(x,False)):
                st.append(x)
            elif(not bool(d.get(x,False))):
                if(len(st)<1):
                    return False
                if(d[st[-1]] == x):
                    st.pop()
                else:
                    return False
        if(len(st)==0):
            return True
        else:
            return False
                
    
        
        