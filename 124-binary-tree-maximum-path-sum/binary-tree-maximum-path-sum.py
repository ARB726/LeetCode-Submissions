# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        self.maximum = float('-inf')

        self.helperFunction(root)

        return self.maximum


    def helperFunction(self,node):
        if not node:
            return 0

        left = max(0 , self.helperFunction(node.left))

        right = max(0 , self.helperFunction(node.right))

        self.maximum = max(self.maximum , left + right + node.val)

        return max(left , right) + node.val