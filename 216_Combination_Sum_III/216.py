class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.answer = []

        def func(path, remain, num):
            if len(path) == k:
                if num == 0:
                    self.answer.append(path)
            else:
                for i in range(len(remain) - k + len(path) + 1):
                    if num < remain[i]:
                        break
                    func(path + [remain[i]], remain[i + 1:], num - remain[i])
        func([], range(1, min(9, n) + 1), n)
        return self.answer
