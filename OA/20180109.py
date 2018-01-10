testing = "NodePair2SRepr"


def SortByBinarySum(nums):
    def BinarySum(num):
        count = 0
        while num:
            count += num & 1
            num = num >> 1
        return (count, num)
    nums.sort(key=BinarySum)


if testing == 'SortByBinarySum':
        # b1,b10,b11,b100,b101,b110,b111,b1000
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    SortByBinarySum(nums)
    print(nums)


def StepOfDigitMove(num1, num2):
    ans = 0
    while num1 or num2:
        digit1 = num1 % 10
        digit2 = num2 % 10
        num1 /= 10
        num2 /= 10
        ans += abs(digit1 - digit2)
    return ans


if testing == 'StepOfDigitMove':
    print(StepOfDigitMove(1234, 4321))


def NodePair2SRepr(ListOfConnections):
    # input: root-node pairs
        #[('B','D'),('D','E'),('A','B'),('C','F'),('E','G'),('A','C')]
    # output: S-expression of trees
        #'E1': more than two child
        #'E2': Duplicate Edges
        #'E3': Cycle present
        #'E4': Multiple roots
        #'E5': Any other error
        # '(A(B(D(E(G))))(C(F)))'
    # above is priority sequence
    error_code = 6
    ans = ''
    # construct tree

    class TreeNode(object):
        def __init__(self, s):
            self.childs = set()
            self.fathers = set()
            self.val = s

        def __repr__(self):
            return self.val + '[' + ''.join([i.val for i in list(self.fathers)]) + '][' + ''.join([i.val for i in list(self.childs)]) + ']'
    # output

    def format_(error_code):
        return 'E' + str(error_code)

    def TreeRootGen(ListOfConnections, error_code):
        TreeNodeMap = {}
        for root, child in ListOfConnections:
            if root not in TreeNodeMap:
                TreeNodeMap[root] = TreeNode(root)
            if child not in TreeNodeMap:
                TreeNodeMap[child] = TreeNode(child)
            if TreeNodeMap[child] in TreeNodeMap[root].childs:
                error_code = min(error_code, 2)
            else:
                TreeNodeMap[root].childs.add(TreeNodeMap[child])
                TreeNodeMap[child].fathers.add(TreeNodeMap[root])
        # check E1,E5
        roots = []
        for node in TreeNodeMap:
            if len(TreeNodeMap[node].childs) > 2:
                error_code = min(error_code, 1)
            if len(TreeNodeMap[node].fathers) > 1:
                error_code = min(error_code, 5)
            if len(TreeNodeMap[node].fathers) == 0:
                roots.append(TreeNodeMap[node])
        return error_code, TreeNodeMap, roots
    # check E4
    error_code, TreeNodeMap, roots = TreeRootGen(ListOfConnections, error_code)
    if len(roots) > 1:
        error_code = min(error_code, 4)
    elif len(roots) == 0:
        error_code = min(error_code, 3)
        return format_(error_code)
    # check E3
    from Queue import Queue
    Q = Queue()
    for root in roots:
        Q.put(root)
    count = 0
    while not Q.empty():
        node = Q.get()
        count += 1
        for child in node.childs:
            child.fathers.remove(node)
            if len(child.fathers) == 0:
                Q.put(child)
    if count < len(TreeNodeMap):
        error_code = min(TreeNodeMap, 3)
    # check error code
    if error_code < 6:
        return format_(error_code)
    # construct S - Representation
    _, TreeNodeMap, roots = TreeRootGen(ListOfConnections, error_code)

    def branch(node):
        if node is None:
            return ""
        else:
            return '(' + node.val + ''.join([branch(key) for key in node.childs]) + ')'
    return ''.join([branch(root) for root in roots])


if testing == 'NodePair2SRepr':
    pairs_lst = []
    pairs_lst.append([('B', 'D'), ('D', 'E'), ('A', 'B'),
                      ('C', 'F'), ('E', 'G'), ('A', 'C')])  # correct
    pairs_lst.append([('B', 'D'), ('D', 'E'), ('A', 'B'),
                      ('C', 'F'), ('E', 'G'), ('A', 'C'), ('A', 'H')])  # E1
    pairs_lst.append([('B', 'D'), ('D', 'E'), ('A', 'B'),
                      ('C', 'F'), ('E', 'G'), ('A', 'C'), ('D', 'E')])  # E2
    pairs_lst.append([('B', 'D'), ('D', 'E'), ('A', 'B'),
                      ('C', 'F'), ('E', 'G'), ('A', 'C'), ('G', 'D')])  # E3
    pairs_lst.append([('B', 'D'), ('D', 'E'), ('A', 'B'),
                      ('C', 'F'), ('E', 'G')])  # E4
    pairs_lst.append([('B', 'D'), ('D', 'E'), ('A', 'B'),
                      ('C', 'F'), ('E', 'G'), ('A', 'C'), ('B', 'F')])  # E5
    for pairs in pairs_lst:
        print(NodePair2SRepr(pairs))

# LC697