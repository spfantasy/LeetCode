from queue import Queue


class Solution:
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        record = [[-1] * len(matrix[0]) for _ in range(len(matrix))]

        def dp(i, j):
            if record[i][j] == -1:
                path_length = [0]
                for _i, _j in zip([1, 0, -1, 0], [0, 1, 0, -1]):
                    ii = i + _i
                    jj = j + _j
                    if 0 <= ii < len(matrix) and 0 <= jj < len(matrix[0]) and matrix[ii][jj] > matrix[i][j]:
                        path_length.append(dp(ii, jj))
                record[i][j] = max(path_length) + 1
            return record[i][j]

        return max([dp(i, j) for i in range(len(matrix)) for j in range(len(matrix[0]))] + [0])
