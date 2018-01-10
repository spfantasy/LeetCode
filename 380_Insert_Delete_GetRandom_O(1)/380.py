class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.index = {}#key -> index
        self.data = []#index -> key

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.index:
            return False
        else:
            self.data.append(val)
            self.index[val] = len(self.data) - 1
            return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.index:
            return False
        else:
            if len(self.data) > 1:
                removed_idx = self.index[val]
                self.data[removed_idx] = self.data[-1]
                self.index[self.data[-1]] = removed_idx
            self.data.pop()
            self.index.pop(val)
            return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        from random import randint
        return self.data[randint(0,len(self.data)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()