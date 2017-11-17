class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        import sys
        if sys.version[0] == "2":
            from Queue import Queue
        else:
            from queue import Queue
        Q = Queue()
        engaged = set()
        row = len(grid)
        if row == 0: 
            return 0
        col = len(grid[0])
        if col == 0:
            return 0
        ans = 0
        for i in range(row):
            for j in range(col):
                # this earth has not been reached
                if (i, j) not in engaged and grid[i][j] == "1":
                    ans += 1
                    Q.put((i, j))
                    engaged.add((i, j))
                    while not Q.empty():
                        x, y = Q.get()
                        for x_, y_ in zip([1,0,-1,0], [0,1,0,-1]):
                            xx = x + x_
                            yy = y + y_
                            if 0<= xx < row and 0 <= yy < col and (xx, yy) not in engaged and grid[xx][yy] == "1":
                                Q.put((xx, yy))
                                engaged.add((xx, yy))
        return ans