fname = "mbox.txt"
f = open(fname)

dic = {}
l = [line.split()[1] for line in f.readlines()
     if line.startswith("From") and line.find("@") > 0 and len(line.split()) > 2]
        #if line.startswith("X-DSPAM-Confidence:")
for i in l:
    if not dic.get(i):
        dic[i] = 1
    else:
        dic[i] +=1

for key in dic.keys():
    print (key, dic[key])