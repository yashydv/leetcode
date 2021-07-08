class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def check(p,q):
            if p is None and q is None:
                return True
            if (p is None and q is not None ) or (p is not None and q is None):
                return False
            if p.val!=q.val:
                return False
            return check(p.left,q.left) and check(p.right,q.right)
        return check(p,q)
