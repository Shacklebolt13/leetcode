class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def check(s,t):
            d = {}
        
            for i,j in zip(s,t):
                if(j not in d):
                    d[j] = i

                else:
                    if(d[j] != i):
                        return False
            if(len(set(d.values())) != len(d.values())):
                return False
            # print(d)
            return True
    
        def _generator(s,t):
            for x in s:
                if(check(x,t)):
                    yield x
    
        return list(_generator(words,pattern))
    