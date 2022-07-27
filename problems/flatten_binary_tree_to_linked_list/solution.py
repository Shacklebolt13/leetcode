# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if(root is not None): 
            ptr = root
            while ptr is not None:
                if(ptr.left is not None):
                    ptr2 = ptr.left
                    while ptr2.right is not None:
                        ptr2 = ptr2.right

                    tmp = ptr.right
                    ptr.right = ptr.left
                    ptr2.right = tmp
                    ptr.left = None

                ptr = ptr.right
        
                
                    