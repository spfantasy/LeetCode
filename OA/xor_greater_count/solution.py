'''
Given a list of integer 1 - 2^32 and a threshold m
count pair of integers whose xor is greater than m
'''


class Solution:
    def xor_greater_than(self, nums, m):
        # get maximum length of number in nums and m
        max_digit = self.get_max_digit(nums + [m])
        # Create root of Trie
        T = BinaryTrieNode(max_digit)
        ans = 0
        for num in nums:
            '''
            based on current number, iteratively go down to find N
            s.t. num ^ N = m
            '''
            Trie_ptr = T
            # go from highest to lowest
            for i in reversed(range(max_digit)):
                # i th digit of num
                digit = (num >> i) & 1
                # i th digit of m
                m_digit = (m >> i) & 1
                # num ^ N = m -> num ^ m = N
                # get i th digit of N
                target = m_digit ^ digit
                # choose different digit on N would make m greater?
                if m_digit == 0:
                    # then add all numbers in that branch
                    ans += Trie_ptr.get(1 - target).count
                # go deeper to check next digit
                Trie_ptr = Trie_ptr.get(target)
            # append current number to Trie
            T.add(num)
        return ans

    def get_max_digit(self, lst):
        max_digit = 0
        max_num = max(lst)
        while max_num > 0:
            max_num >>= 1
            max_digit += 1
        return max_digit


class BinaryTrieNode:
    def __init__(self, depth):
        self.__data = {}
        self.count = 0
        self.depth = depth

    def get(self, digit):
        if digit not in self.__data:
            self.__data[digit] = BinaryTrieNode(self.depth - 1)
        return self.__data[digit]

    def add(self, num):
        currentNodePtr = self
        currentNodePtr.count += 1
        for i in reversed(range(self.depth)):
            digit = (num >> i) & 1
            currentNodePtr = currentNodePtr.get(digit)
            currentNodePtr.count += 1


if __name__ == "__main__":
    S = Solution()
    # print(S.get_max_digit([1, 2, 3, 4, 5, 6, 7]))
    ans = 0
    for i in [2, 3, 5, 7, 11, 13, 17, 19]:
        for j in [2, 3, 5, 7, 11, 13, 17, 19]:
            if i < j and i ^ j > 8:
                ans += 1
    print(ans)


A = obj()
A.put
