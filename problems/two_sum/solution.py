class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for num, index  in zip(nums,range(10000)):
            mirror = target - num
            m_index = d.get(mirror,None)
            if(m_index is not None):
                return [m_index,index]
            else:
                d[num] = index
                               
                    