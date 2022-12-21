import pickle
from datetime import datetime
import matplotlib.pyplot as plt


class NuT:
    def __init__(self, message="", type=0, check=False, datetime=datetime.now().strftime("%H:%M")):
        self.message = message
        self.type = type
        self.check = check
        self.datetimedev = datetime
        self.tags = self.tags_searcher(self.message)

    def tags_searcher(self, str_with_tags):
        list_of_tags = []
        for elem in str_with_tags.split("#")[1:]:
            local_str = ""
            for char in elem:
                if not (char in [" ", ",", ".", "\n", "!", "?", "^", "\t"]):
                    local_str += char
                else:
                    list_of_tags.append(local_str)
                    break
            if local_str == elem:
                list_of_tags.append(elem)
        return sorted(list_of_tags)

    def give_with_date_and_sl_n(self):
        return self.message + "\t" * 5 + "|" + self.datetime + "|" + "\n"


class List_of_NuT:
    def __init__(self, date=datetime.now().strftime("%d.%m.%Y"), list_of_nuts=[]):
        self.list_of_tags = set()
        if datetime != datetime.now().strftime("%d-%b-%Y"):
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
                self.date = datetime.now().strftime("%d-%b-%Y")
                self.list_of_tags.add("Today")
        else:
            self.date = datetime.now().strftime("%d-%b-%Y")
            self.list_of_tags.add("Today")

        nt_fo_type = NuT()
        for elem in list_of_nuts:
            if type(elem) != type(nt_fo_type):
                list_of_nuts.remove(elem)
                print("ONE OF VALUE NOT IS NUT! THS VAL WAS DEL!")
        self.list_of_nuts = list_of_nuts

        if self.list_of_nuts != []:
            self.tags_appender(self.list_of_tags, self.list_of_nuts)

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

    def give_prevue(self, n=40, flag_of_date=False):
        message = ""
        for elem in self.list_of_nuts:
            if len(message) < n:
                message += elem.message + "\n"
            else:
                break
        message = message[:n]
        if flag_of_date:
            return message + "\t" * 5 + "|" + self.date + "|" + "\n"
        else:
            return message


class All_Nut:
    def __init__(self, list_of_nuts=[]):
        self.all_nuts_tags = set()
        nt_fo_type = List_of_NuT()
        for elem in list_of_nuts:
            if type(elem) != type(nt_fo_type):
                print(elem, list_of_nuts, 42)
                list_of_nuts.remove(elem)
                print("ONE OF VALUE NOT IS NUT! THS VAL WAS DEL!")
        self.list_of_nuts = list_of_nuts
        if self.list_of_nuts != []:
            self.tags_appender(self.all_nuts_tags, self.list_of_nuts)

    def tags_appender(self, list_of_tags, all_nuts_tags):
        for elem in all_nuts_tags:
            for tag in elem.list_of_tags:
                list_of_tags.add(tag)
        sorted(list_of_tags)

    def all_nut_appender(self, date=datetime.now().strftime("%Y.%m.%d"), list_of_nuts=[], list_in_today=None):
        if list_in_today == None:
            self.list_of_nuts.append(List_of_NuT(date, list_of_nuts))
        else:
            self.list_of_nuts.append(list_in_today)
        self.tags_appender(self.all_nuts_tags, self.list_of_nuts)

    def sorted_by_date(self, reverse=True):
        if reverse:
            return sorted(self.list_of_nuts, key=lambda x: x.date)
        else:
            return sorted(self.list_of_nuts, key=lambda x: x.date).reverse()

    def searcher(self, search_by=""):
        if search_by == "":
            return []
        elif search_by[0] == "#":
            returned = []
            for elem in self.list_of_nuts:
                print(search_by[1:], elem.list_of_tags)
                if search_by[1:] in elem.list_of_tags:
                    returned.append(elem)
            return returned
        else:
            returned = []
            for elem in self.list_of_nuts:
                local_str = elem.give_prevue(1000)
                if local_str.count(search_by) > 0:
                    returned.append(elem)
            return returned

    def give_stats(self):
        counter = 0
        for elem in self.list_of_nuts:
            for eleme in elem.list_of_nuts:
                if eleme.type in [2, 3]:
                    counter += 1

        tr = 0
        fl = 1
        counter = 0

        fig, ax = plt.subplots()
        y1 = []
        xs = [0, 0]
        ys = [0.5, 0.5]
        plt.ion()
        plt.title("stats")
        plt.ylabel("NoOfNuT")
        plt.xlabel("% of success")
        for elem in self.list_of_nuts:
            for eleme in elem.list_of_nuts:
                if eleme.type in [2, 3]:
                    counter += 1
                    if eleme.check == False:
                        tr += 1
                    else:
                        fl += 1
                    xs[0] = xs[1]
                    ys[0] = ys[1]
                    xs[1] = counter
                    ys[1] = tr / (tr + fl)
                    plt.plot(xs, ys)
                    plt.pause(1)
        plt.pause(1000)
        print(tr, fl)

    def save_file_by_pikle(self, file):
        with open('data.pickle', 'wb') as f:
            pickle.dump(file, f)

    def load_file_by_pikle(self):
        with open('data.pickle', 'rb') as f:
            return pickle.load(f)
