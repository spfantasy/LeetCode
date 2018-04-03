from Queue import Queue


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        Q = Queue()
        Q.put(self)
        ans = []
        while not Q.empty():
            pool = []
            while not Q.empty():
                pool.append(Q.get())
            if all([node is None for node in pool]):
                break
            else:
                for node in pool:
                    if node is None:
                        ans.append('[]')
                        Q.put(None)
                        Q.put(None)
                    else:
                        ans.append(str(node.val))
                        Q.put(node.left)
                        Q.put(node.right)
                ans.append('\n')
        return ' '.join(ans)


def TernaryExpr2Tree(string):
        # a?b?c:d:e
    stack = []
    if len(string) == 0:
        return None
    # generate items
    i = j = 0
    items = []
    while i < len(string):
        while i < len(string) and string[i] not in [':', '?']:
            i += 1
        items.append(string[j:i])
        if i != len(string):
            items.append(string[i])
        j = i + 1
        i += 1
    # build root
    root = TreeNode(items[0])
    stack.append(root)
    i = 1
    while i < len(items):
        sym = items[i]
        val = items[i + 1]
        i += 2
        node = TreeNode(val)
        if sym == '?':
            stack[-1].left = node
            stack.append(node)
        else:
            stack.pop()
            while stack[-1].right:
                stack.pop()
            stack[-1].right = node
            stack.append(node)
    return root


root = TernaryExpr2Tree('a?b?d:e:c?f:g')
print(root)
