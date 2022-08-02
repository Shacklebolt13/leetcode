class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        d = set()
        st = 0
        x = 0
        maxm = 0
        count = 0
        l = len(s)
        while x < l:
            # print(s[x],end=":")
            
            if(s[x] not in d):
                # print(end="! ")
                d.add(s[x])
                count+=1
                x+=1
                # print(count,maxm,end=" ")
            else:
                # print(s[x])
                d.remove(s[st])
                st+=1
                count-=1
                
            if(maxm<=count):
                maxm = count
                
            # print()
        
                
        return maxm