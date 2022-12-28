import pickle
from datetime import datetime
import matplotlib.pyplot as plt

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
        return sorted(list_of_tags)

    def give_with_date_and_sl_n(self):
        return self.message + "\t" * 5 + "|" + self.datetime + "|" + "\n"

