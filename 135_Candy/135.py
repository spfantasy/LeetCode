class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if len(ratings) == 0:
            return 0
        answer = [1] * len(ratings)
        for i in range(len(ratings)):
            if i > 0 and ratings[i] > ratings[i-1]:
                answer[i] = answer[i-1]+1
        for i in range(len(ratings))[::-1]:
            if i < len(ratings) - 1 and ratings[i] > ratings[i+1]:
                answer[i] = max(answer[i], answer[i+1] + 1)
        return sum(answer)