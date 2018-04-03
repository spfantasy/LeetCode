class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        def traverse(node, t1, t2):
            if (t1 and t1.left) or (t2 and t2.left):
                left_val = 0
                if t1 and t1.left:
                    left_node_1 = t1.left
                    left_val += left_node_1.val
                else:
                    left_node_1 = None
                if t2 and t2.left:
                    left_node_2 = t2.left
                    left_val += left_node_2.val
                else:
                    left_node_2 = None
                node.left = TreeNode(left_val)
                traverse(node.left, left_node_1, left_node_2)
            if (t1 and t1.right) or (t2 and t2.right):
                right_val = 0
                if t1 and t1.right:
                    right_node_1 = t1.right
                    right_val += right_node_1.val
                else:
                    right_node_1 = None
                if t2 and t2.right:
                    right_node_2 = t2.right
                    right_val += right_node_2.val
                else:
                    right_node_2 = None
                node.right = TreeNode(right_val)
                traverse(node.right, left_node_1, left_node_2)
        initial_val = 0
        if t1:
            initial_val += t1.val
        if t2:
            initial_val += t2.val
        root = TreeNode(initial_val)
        traverse(root, t1, t2)
        return root

    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # char -> num
        count = {}
        # max length
        ans = 0

        start = -1
        for end in range(len(s)):
            count[s[end]] = count.get(s[end], 0) + 1
            maximum = max(list(count.values()))
            while maximum < end - start - k:
                start += 1
                count[s[start]] -= 1
            ans = max(ans, end - start)
        return ans


S = Solution()
print(S.characterReplacement("ABAB", 2))
