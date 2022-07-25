class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        st = None
        end = None
        l = len(nums)
        broken = False
        for i in range(l):
            if(st is None and nums[i]==target):
                st = i
                end = i
            if(nums[i]>target):
                end = i-1
                broken = True
                break
        
        if(broken ==False):
            end = l-1
        if( st is None or end is None):
            return [-1,-1]
        return [st,end]