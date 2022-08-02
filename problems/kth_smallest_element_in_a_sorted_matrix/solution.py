from itertools import chain

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        return  sorted(chain.from_iterable(matrix))[k-1]
        
        
        