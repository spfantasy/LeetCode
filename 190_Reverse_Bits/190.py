class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans = 0
        for i in range(32):
            bit = n % 2
            n /= 2
            ans = ans * 2 + bit
        return ans