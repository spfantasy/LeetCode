class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        reg = p
        record = [[None] * (len(reg) + 1) for _ in range(len(s) + 1)]

        def dp(i, j):
            # return if the s[:i] and p[:j] match
            if i < 0 or j < 0:
                return False
            elif record[i][j] is not None:
                return record[i][j]
            else:
                if i == 0 and j == 0:
                    record[i][j] = True
                elif i != 0 and j == 0:
                    record[i][j] = False
                elif reg[j - 1] == '.':
                    record[i][j] = dp(i - 1, j - 1)
                elif reg[j - 1] != '*':
                    record[i][j] = dp(i - 1, j - 1) and reg[j - 1] == s[i - 1]
                else:
                    if reg[j - 2:j] == '.*':
                        record[i][j] = dp(i, j - 2) or dp(i - 1, j)
                    else:
                        matcher = reg[j - 2]
                        record[i][j] = dp(
                            i, j - 2) or (dp(i - 1, j) and s[i - 1] == matcher)
                return record[i][j]
        return dp(len(s), len(p))
