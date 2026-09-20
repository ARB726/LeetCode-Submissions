# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        def helperFunction(node):
            if not node:
                return 0

            left = helperFunction(node.left)
            right= helperFunction(node.right)

            if left == -1 or right == -1 : return -1

            if abs(right-left) > 1: return -1
            
            else: return max(left,right)+1
            
        if helperFunction(root) == -1: return False
        
        else:return True