from queue import Queue


class Solution:
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        class Node(object):
            def __init__(self, val):
                self.val = val
                self.root = set()
                self.leaf = set()
            def __repr__(self):
                return str(self.val)+str([itm.val for itm in list(self.root)])+str([itm.val for itm in list(self.leaf)])
        Q=Queue()
        #establish words dict
        nodedict = {}
        words = [' '] + words
        for i in range(len(words)):
            for j in range(len(words[i])):
                if words[i][j] not in nodedict:
                    nodedict[words[i][j]] = Node(words[i][j])
        #add relationship
        for i in range(len(words) - 1):
            A = words[i] + ' '
            B = words[i + 1] + ' '
            for j in range(min(len(A), len(B))):
                ca = A[j]
                cb = B[j]
                if ca != cb:
                    if ca not in nodedict[cb].root:
                        nodedict[cb].root.add(nodedict[ca])
                    if cb not in nodedict[ca].leaf:
                        nodedict[ca].leaf.add(nodedict[cb])
                    break
        #pop roots and remove dependency
        for node in nodedict.values():
            # print(node)
            if len(node.root) == 0:
                Q.put(node)
        ans = ""
        while not Q.empty():
            node = Q.get()
            ans += node.val
            for l in node.leaf:
                l.root.remove(node)
                if len(l.root) == 0:
                    Q.put(l)
        #check all character in answer
        if len(ans) != len(nodedict):
            return ""
        else:
        	#remove space
            return ''.join(ans.split(' '))
