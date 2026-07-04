# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        if root:
            res.append(root.val)
        else:
            return []

        q = deque()
        q.append(root.right)
        q.append(root.left)

        while q:
            qlen = len(q)
            check = False
            for _ in range(qlen):
                curr = q.popleft()
                if curr:
                    if not check:
                        res.append(curr.val)
                        check = True
                    if curr.right:
                        q.append(curr.right)
                    if curr.left:
                        q.append(curr.left)

        return res
