fname = "mbox.txt"
file = open(fname)
adr = all_mail = Conf = all_Conf = spam = 0
a = set()
l = [line.split() for line in file if line.startswith("From ") and line.find("@") > 0 and len(line.split()) > 2]
file.closed
file = open(fname)
k = [line.split()for line in file if line.startswith("X-DSPAM-Confidence:")]
for i in range(len(k)):
    adr = (l[i][1])
    Conf = k[i][1]
    all_Conf += float(Conf)
    all_mail += 1
    spam = all_Conf/all_mail
    print("по адресу:", adr, "значение X-DSPAM-Confidence равно:", Conf)
    if float(Conf) >= 0.96:
        a.add(adr)
    else:
        continue
for i in a:
    print("Забанить - ", i)
print("Всего писем:", all_mail, "Среднее значение X-DSPAM-Confidence:", spam, "Забанить за спам нужно:", len(a))