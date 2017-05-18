import math
import pylab
import pickle
import csv
R = 36.4
n = 100
x= 0
list = []
dic = {}
while x < n:
    x += 0.01
    y = 452*(math.cos(x/11)+math.cos(x/8))+R+175
    if not dic.get(y):
        dic[y] = round(x * 100, 1)
#for key in dic.keys():
    #print (key, dic[key])
#print(dic)
for i in dic.keys():
    list.append(i)
#print(list)

with open('ttt.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    for i in dic.items():
        csv_writer.writerow([i])



#import math
## Импортируем один из пакетов Matplotlib
#import pylab
## Импортируем пакет со вспомогательными функциями
#from matplotlib import mlab
#
#
## Рисуем график функции y = sin(x)
#def func(x):
#    """
#    sin (x)
#    """
#    return 452*(math.cos(x/11)+math.cos(x/8))+R+175
#
#
## Указываем X наименьее и наибольшее
#xmin = 1
#xmax = 10000.0
#
## Шаг между точками
#dx = 1
#
## Создадим список координат по оси
## X на отрезке [-xmin; xmax], включая концы
#xlist = mlab.frange(xmin, xmax, dx)
#
## Вычислим значение функции в заданных точках
#ylist = [func(x) for x in xlist]
#
## Нарисуем одномерный график
#pylab.plot(xlist, ylist)
#
## Покажем окно с нарисованным графиком
#pylab.show()#