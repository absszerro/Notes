import pickle
from datetime import datetime
import matplotlib.pyplot as plt
from NuT import NuT


class List_of_NuT:
    def __init__(self, date=datetime.now().strftime("%d.%m.%Y"), list_of_nuts=[]):
        self.list_of_tags = set()
        if date != datetime.now().strftime("%d.%m.%Y"):
            try:
                str_date = date[:2] + "." + date[3:5] + "." + date[6:10]
                print(str_date, 1)
                self.date = (datetime.strptime(str_date, '%d.%m.%Y').date().strftime("%Y.%m.%d"))
                if self.date > datetime.now().strftime("%Y.%m.%d"):
                    self.list_of_tags.add("Futures_plans")
                else:
                    self.list_of_tags.add("Pasts")
            except Exception:
                print("ERROR! INPUT MUST BE LIKE 01.02.2003! BE INCLUDED TODAY DAYTIME!")
                self.date = datetime.now().strftime("%Y.%m.%d")
                self.list_of_tags.add("Today")
        else:
            self.date = datetime.now().strftime("%Y.%m.%d")
            self.list_of_tags.add("Today")

        nt_fo_type = NuT()
        for elem in list_of_nuts:
            if type(elem) != type(nt_fo_type):
                print(type(elem), type(nt_fo_type))
                list_of_nuts.remove(elem)
                print("ONE OF VALUE NOT IS NUT! THS VAL WAS DEL!")
        self.list_of_nuts = list_of_nuts

        if self.list_of_nuts != []:
            self.tags_appender(self.list_of_tags, self.list_of_nuts)

        self.all_checked, self.true_checked, self.false_checked = self.stats_give()

    def stats_give(self):
        counter, tr, fl = 0, 0, 0
        for eleme in self.list_of_nuts:
            if eleme.type in [2, 3]:
                counter += 1
                if not eleme.check:
                    tr += 1
                else:
                    fl += 1
        return (counter, tr, fl)

    def tags_appender(self, list_of_tags, list_of_nuts):
        for elem in list_of_nuts:
            for tag in elem.tags:
                list_of_tags.add(tag)
        sorted(list_of_tags)

    def NuTs_appender(self, message="", type=0, check=False, datetime=datetime.now().strftime("%H:%M"), NuTs=None):
        if NuTs == None:
            self.list_of_nuts.append(NuT(message, type, check, datetime))
        else:
            self.list_of_nuts.append(NuTs)
        self.tags_appender(self.list_of_tags, self.list_of_nuts)

    def give_prevue(self, n=40, flag_of_date=False, give_text=True):
            message = ""
            for elem in self.list_of_nuts:
                if len(message) < n:
                    message += elem.message + "\n"
                else:
                    break
            message = message[:n]
            if give_text:
                if flag_of_date:
                    return message + "\t" * 5 + "|" + self.date + "|" + "\n"
                else:
                    return message
            else:
                return [self.date, str(self.true_checked) + "/" + str(self.all_checked), message]
