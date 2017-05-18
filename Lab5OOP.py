class Mail:
    adr = all_mail = Conf = all_Conf = spam = 0
    a = set()
    def search1(self,fname):
        file = open(fname)
        l = [line.split() for line in file if line.startswith("From ") and line.find("@") > 0 and len(line.split()) > 2]
        file.closed
        return  l
    def search2(self, fname):
        file = open(fname)
        k = [line.split() for line in file if line.startswith("X-DSPAM-Confidence:")]
        file.closed
        return k
mail = Mail()

for i in range(len(mail.search1('mbox.txt'))):
    mail.adr = (mail.search1('mbox.txt')[i][1])
    mail.Conf = mail.search2('mbox.txt')[i][1]
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
print("Всего писем:", mail.all_mail, "Среднее значение X-DSPAM-Confidence:", mail.spam, "Забанить за спам нужно:", len(mail.a))
