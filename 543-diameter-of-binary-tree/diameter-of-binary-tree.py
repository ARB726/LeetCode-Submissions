# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dia=0
        def d(node):
            #dia=0
            if not node:
                return 0
            node_left=d(node.left)
            node_right=d(node.right)
            self.dia=max(self.dia,node_left+node_right)
            return 1+max(node_left,node_right)
        d(root)
        return self.dia