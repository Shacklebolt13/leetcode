class Solution:
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = len(strs)
        if(l==1):
            return strs[0]
        pref = self.commonPrefix(strs[0],strs[1])
        
        for x in strs[2:]:
            pref = self.commonPrefix(pref,x)
        
        return pref
    
    
    
    def commonPrefix(self,str1,str2):
        l2 = len(str2)
        l1 = len(str1)
        
        ans = 0
        
        if(l1>l2):
            print('case1')
            for i in range(0,l2):
                ans = i
                if(str1[i] != str2[i]):
                    break
            else:
                ans+=1 if l2>=1 else 0
                
        else:
            print('case2')
            for i in range(0,l1):
                ans = i
                if(str1[i] != str2[i]):
                    break
            else:
                ans+=1 if l1>=1 else 0
        print(ans)
        return str1[:ans]
            
            
            
            