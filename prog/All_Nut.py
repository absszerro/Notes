import pickle
from datetime import datetime
import matplotlib.pyplot as plt
from List_of_NuT import List_of_NuT

class All_Nut:
    def __init__(self, list_of_nuts = []):
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

    def all_nut_appender(self, date=datetime.now().strftime("%Y.%m.%d"), list_of_nuts = [], list_in_today = None):
        self.list_of_nuts.append(List_of_NuT(date, list_of_nuts))
        self.tags_appender(self.all_nuts_tags, self.list_of_nuts)

    def sorted_by_date(self, reverse = True):
        if reverse:
            return list(sorted(self.list_of_nuts, key=lambda x: x.date))
        else:
            return list(reversed(sorted(self.list_of_nuts, key=lambda x: x.date)))

    def searcher(self, search_by = ""):
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
                    ys[1] = tr/(tr+fl)
                    plt.plot(xs, ys)
                    plt.pause(0.5)
        plt.pause(1000)
        print(tr, fl)

    def save_file_by_pikle(self, file):
        with open('data.pickle', 'wb') as f:
            pickle.dump(file, f)

    def load_file_by_pikle(self):
        with open('data.pickle', 'rb') as f:
            return pickle.load(f)