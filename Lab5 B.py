adr = all_mail = Conf = all_Conf = spam = 0
a = set()
s1 = "From"
s2 = "X-DSPAM-Confidence:"
fname = "mbox.txt"
def search(fname, str):
    fname = fname
    file = open(fname)
    search = [line.split() for line in file if line.startswith(str)]
    file.closed
    return search
l = search(fname, s1)
k = search(fname, s2)
for i in range(len(k)):
    adr = l[i][1]
    Conf = k[i][1]
    all_Conf += float(Conf)
    all_mail += 1
    spam = all_Conf/all_mail
    print("по адресу:", adr, "значение X-DSPAM-Confidence равно:", Conf)
    if float(Conf) >= spam:
        a.add(adr)
    else:
        continue
for i in a:
    print("Забанить - ", i)
print("Всего писем:", all_mail, "Среднее значение X-DSPAM-Confidence:", round(spam, 4), "Забанить за спам нужно:", len(a))