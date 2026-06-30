# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val=val)

        prev = None
        curr = root

        while curr:
            prev = curr
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right

        if val < prev.val:
            prev.left = TreeNode(val=val)
        else:
            prev.right = TreeNode(val=val)

        return root
