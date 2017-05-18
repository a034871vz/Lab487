def sort(dic):
    result = sorted(dic.items(), key=lambda x: x[1])
    return result
fname = "mbox.txt"
f = open(fname)
dic = {}
l = [line.split()[1] for line in f.readlines()
     if line.startswith("From") and line.find("@") > 0 and len(line.split()) > 2]
print(l)
        #if line.startswith("X-DSPAM-Confidence:")
for i in l:
    if not dic.get(i):
        dic[i] = 1
    else:
        dic[i] += 1


l1 = [line.split()[1] for line in f.readlines()
      if line.startswith("From ") and line.find("@") > 0 and len(line.split()) > 2]
print(l1)

#for key, value in dic.items():
#        print(key, value)
