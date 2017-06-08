class Mail:
    adr = all_mail = Conf = all_Conf = spam = 0
    a = set()
    def Search(self, fname, str):
        self.fname = fname
        file = open(self.fname)
        search = [line.split() for line in file if line.startswith(str)]
        file.closed
        return search
mail = Mail()
s1 = "From"
s2 = "X-DSPAM-Confidence:"
fname = "mbox.txt"
mail.l = mail.Search(fname, s1)
mail.k = mail.Search(fname, s2)
for i in range(len(mail.k)):
    mail.adr = mail.l[i][1]
    mail.Conf = mail.k[i][1]
    mail.all_Conf += float(mail.Conf)
    mail.all_mail += 1
    mail.spam = mail.all_Conf/mail.all_mail
    print("по адресу:", mail.adr, "значение X-DSPAM-Confidence равно:", mail.Conf)
    if float(mail.Conf) >= 0.96:
        mail.a.add(mail.adr)
    else:
        continue
for i in mail.a:
    print("Забанить - ", i)
print("Всего писем:", mail.all_mail, "Среднее значение X-DSPAM-Confidence:", round(mail.spam, 4), "Забанить за спам нужно:", len(mail.a))