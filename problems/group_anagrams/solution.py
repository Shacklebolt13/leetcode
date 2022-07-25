class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = {}
        while strs:
            tmp = strs.pop()
            tmps = "".join(sorted(tmp))
            
            if(tmps in d):
                d[tmps].append(tmp)
            else:
                d[tmps] = [tmp]
                
        return list(d.values())
            
            
        