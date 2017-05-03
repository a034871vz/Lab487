import matplotlib.pyplot as plt
fname = "mbox.txt"
f = open(fname)

dic = {}
maxvalue = 0
name = ""
l = [i.split()[1] for i in f.readlines()
            if i.startswith("From") and i.find("@")>0 and len(i.split()) > 2]
for i in l:
    if not dic.get(i):
        dic[i] = 1
    else:
        dic[i] +=1
        if maxvalue < dic[i]:
            maxvalue = dic[i]
            name = i

for key in dic.keys():
    print (key, dic[key])