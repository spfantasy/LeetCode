class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        def helper(x, y):
            if x[0] != y[0]:
                return y[0] - x[0]
            else:
                return x[1] - y[1]
        for i in range(len(people) - 1):
            print(helper(people[i], people[i + 1]))
        people.sort(cmp=helper)
        print(people)


S = Solution()
people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
S.reconstructQueue(people)
