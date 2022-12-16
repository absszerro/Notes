from datetime import datetime


class NuT:
    def __init__(self, message="", type=0, check=False, datetime=datetime.now().strftime("%H:%M")):
        self.message = message
        self.type = type
        self.check = check
        self.datetime = datetime
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
        return list_of_tags

    def give_with_date_and_sl_n(self):
        return self.message + "\t" * 5 + "|" + self.datetime + "|" + "\n"

class List_of_NuT:
    def __init__(self, date=datetime.now().strftime("%d.%m.%Y"), list_of_nuts = []):
        self.list_of_tags = set()
        if datetime != datetime.now().strftime("%d-%b-%Y"):
            try:
                str_date = date[:2] + "." + date[3:5] + "." + date[6:10]
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

    def NuTs_appender(self, message="", type=0, check=False, datetime=datetime.now().strftime("%H:%M"), NuTs = None):
        if NuTs == None:
            self.list_of_nuts.append(NuT(message, type, check, datetime))
        else:
            self.list_of_nuts.append(NuTs)
        self.tags_appender(self.list_of_tags, self.list_of_nuts)

    def give_prevue(self, n = 20, flag_of_date = False):
        message = ""
        for elem in self.list_of_nuts:
            if len(message) < n:
                message += elem.message
            else:
                break
        message = message[:n]
        if flag_of_date:
            return message + "\t" * 5 + "|" + self.date + "|" + "\n"
        else:
            return message

class All_Nut:
    pass


class Stats:
    pass
