# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.Result = 0

        def helperFunction(node):
            if not node: return 0

            left = helperFunction(node.left)
            right = helperFunction(node.right)

            self.Result = max(self.Result , left + right)

            return 1 + max(left , right)

        helperFunction(root)

        return self.Result