class SQRT:
    def sqrt(self,num):
        self.a = num
        self.res = len(str(self.a)) + 5
        for i in range(self.res):
            self.res = 1 / 2 * (self.res + self.a / self.res)
        return self.res
s = SQRT()
print('Введите число:')
a = int(input())
print(round(s.sqrt(a), 3))
