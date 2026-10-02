# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.Height = 0
        self.Diameter = 0

        def helperFunction(node):

            if not node:
                return 0

            left = helperFunction(node.left)
            right = helperFunction(node.right)

            self.Height = 1 + max(left,right)

            self.Diameter = max(self.Diameter , left + right)

            return self.Height
        helperFunction(root)
        return self.Diameter
















"""
NOTES
-> ORDER->POSTORDER(left->right->root) - hint: root is not necessary

->
    -We will need a variable that stores the height so that we can pass maxHeight to the diameter
    - THen we will need max To the diamater with left + right

"""


    