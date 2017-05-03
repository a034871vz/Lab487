class Pol:
    res = 0
    def poly(self,list):
        self.a = list
        for i in range(len(self.a)):
            self.res += 1 / (self.a[i] * 3)
        return self.res
p = Pol()
a = [int(i) for i in input().split()]
print(p.poly(a))