class CrossBuilder:
    def __init__(self):
        self.data = {1: ['o']}

    def build(self, n):
        if n - 1 not in self.data:
            self.build(n - 1)
        prev = self.data[n - 1]
        self.data[n] = []
        for row in prev:
            self.data[n].append(' ' * (3**(n - 2)) + row)
        for row in prev:
            self.data[n].append((row + ' ' * ((3**(n - 2) - len(row)))) * 3)
        for row in prev:
            self.data[n].append(' ' * (3**(n - 2)) + row)

    def prt(self, n):
        if n not in self.data:
            self.build(n)
        for row in self.data[n]:
            print(row)
            
num = raw_input()
C = CrossBuilder()
for i in range(num):
    target = raw_input()
    print("Case #{}:".format(i+1))
    C.prt(target)