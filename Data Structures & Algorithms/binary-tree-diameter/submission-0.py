# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def height(root: Optional[TreeNode]) -> int:
            nonlocal ans

            if root is None:
                return 0

            left_height = height(root.left)
            right_height = height(root.right)

            curr_diam = left_height + right_height
            ans = max(ans, curr_diam)

            return 1 + max(left_height, right_height)

        height(root)

        return ans
