def sum(a):
    res = 0
    for i in a:
        res += i
    return res
def sub(a):
    res = a[0]
    for i in range(len(a) - 1):
        res -= a[i + 1]
    return res
def div(a):
    res = a[0]
    for i in range(len(a)-1):
        res /= a[i+1]
    return res
def mult(a):
    res = a[0]
    for i in range(len(a) - 1):
        res *= a[i + 1]
    return res
def res(op):
    if op == '+':
        return sum(a)
    if op == '-':
        return sub(a)
    if op == '/':
        return div(a)
    if op == '*':
        return mult(a)

while 1:
    print('Введите операнды:')
    a = [int(i) for i in input().split()]
    print('Выберите операцию:')
    op = input()
    print(res(op))
    print('Для работы с реузльтатом нажмите >p<, для новых расчетов >n<, для выхода >x<')
    i = input()
    if i == 'x':
        exit(0)
    if i == 'n':
        continue
    if i == 'p':
        a[0]= res(op)
        continue


result = 0
while 1:
    op = str(input())
    if op.startswith("*") or op.startswith("/"):
        result = eval(str(result)+op)
    else:
        result += eval(op)
    print(result)
