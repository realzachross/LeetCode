class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q, qVals = [root], [[root.val]]
        while q:
            newQ, newQVals = list(), list()
            for node in q:
                if node.left:
                    newQ += [node.left]
                    newQVals += [node.left.val]
                if node.right:
                    newQ += [node.right]
                    newQVals += [node.right.val]
                q = newQ
            if newQVals:
                qVals += [newQVals]
        return qVals
