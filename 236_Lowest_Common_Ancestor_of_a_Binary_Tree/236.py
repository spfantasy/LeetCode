# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        from Queue import Queue
        Q = Queue()
        if root:
            Q.put([root])
        path = []
        while not Q.empty() and len(path) < 2:
            node_path = Q.get()
            if node_path[-1] == p or node_path[-1] == q:
                path.append(node_path)
            if node_path[-1].left:
                Q.put(node_path + [node_path[-1].left])
            if node_path[-1].right:
                Q.put(node_path + [node_path[-1].right])

        for i in range(min(len(path[0]), len(path[1]))):
            if path[0][i] != path[1][i]:
                return path[0][i - 1]
        return path[0][i]


if __name__ == "__main__":
    t11 = TreeNode(1)
    t21 = TreeNode(2)
    t11.left = t21
    S = Solution()
    print(S.lowestCommonAncestor(t11, t11, t21))
