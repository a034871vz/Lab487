fname = "mbox.txt"
file = open(fname)
count = 0
l = [line.split() for line in file
     if line.startswith("From") and line.find("@") > 0 and len(line.split()) > 2]
for i in sorted(l):
    print (i[1])
    count+=1
print ("There were", count, "lines in the file with From as the first word")