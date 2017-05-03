def sqrt(a):
    res = len(str(a)) + 5
    for i in range(res):
        res = 1 / 2 * (res + a / res)
    return res
print('Введите число:')
a = int(input())
print(round(sqrt(a), 3))