class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:  # Found the node to delete
            if not root.left:
                return root.right       # Case 1: no left child
            if not root.right:
                return root.left        # Case 2: no right child

            # Case 3: both children exist
            temp = root.left
            while temp.right:
                temp = temp.right
            temp.right = root.right
            return root.left            # Return the new subtree root

        return root