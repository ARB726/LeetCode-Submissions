# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        self.Result = float('-inf')

        self.helperFunction(root)

        return self.Result

    def helperFunction(self,node):

        if not node:
            return 0

        left = max(0 , self.helperFunction(node.left))

        right = max(0 , self.helperFunction(node.right))

        self.Result = max(self.Result , left + right + node.val)

        return node.val + max(left,right)