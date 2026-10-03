# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        self.Result = float('-inf')
        def helperFunction(node):
            if not node:
                return 0

            left = helperFunction(node.left)
            right = helperFunction(node.right)

            self.CurrentMax = node.val + max(0,left) + max(0,right)

            self.Result = max(self.Result , self.CurrentMax)

            return node.val + max(0,left,right)

        helperFunction(root)
        return self.Result






"""
NOTES
- PostOrder -> Left->Root->Right
we will need a helperFunction as well
we will need a max node value that will be passed to global variable to store the value
"""
