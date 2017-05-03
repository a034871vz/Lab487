def poly(a):
    res = 0
    for i in range(len(a)):
        res += 1 / (a[i] * 3)
    return res
a = [int(i) for i in input().split()]
print(poly(a))
