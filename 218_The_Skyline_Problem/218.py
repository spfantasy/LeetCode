class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        from queue import PriorityQueue
        Q = PriorityQueue()
        points = sorted(list(set([b[0] for b in buildings]+[b[1] for b in buildings])))
        # itr points to the leftmost building not been considered
        itr = 0
        # p is the place where we are looking at
        for p in points:
            # add all buildings into PriorityQueue
            while itr < len(buildings) and buildings[itr][0] <= p:
                height = buildings[itr][2]
                rx = buildings[itr][1]
                Q.put((-height, rx))
                itr += 1
            # ensure the highest building still exist
            while not Q.empty():
                h, r = Q.get()
                h = -h
                if r <= p:
                    continue
                else:
                    Q.put((-h, r))
                    break
            # if Q is empty, h should be 0
            h = 0 if Q.empty() else h
            # insert the point into answer if the previous is not the same height
            if len(ans) == 0 or ans[-1][1] != h:
                ans.append([p, h])
        return ans