from NuT import NuT
from List_of_NuT import List_of_NuT
from All_Nut import All_Nut

N = NuT("#start with     #Som#e Text and #tags", type=2, check=True)
B = NuT("Yea", type=2, check=False)
C = NuT("j#wow this work", type=3, check=(True, False, True))
D = NuT("For Test")
Na = NuT("#start with     #Som#e Text and #tags", type=2, check=False)
Nb = NuT("#start with     #Som#e Text and #tags", type=2, check=False)
Nc = NuT("#start with     #Som#e Text and #tags", type=2, check=True)
Nd = NuT("#start with     #Som#e Text and #tags", type=2, check=True)
Ne = NuT("#start with     #Som#e Text and #tags, #and", type=3, check=(False, False, False))
print(N.tags)
print(N.give_with_date_and_sl_n())

Ln = List_of_NuT("01.02.2002", [N, B])
Lb = List_of_NuT("01.02.2025", [C, D])
La = List_of_NuT("01.02.2002", [Na, Nb, Nc, Nd, Ne])

print(Ln.list_of_tags)
print(Lb.list_of_tags)
print(Lb.list_of_nuts)
print(Lb.date)
print(Lb.give_prevue(n=400))

Al = All_Nut([Ln, La])

print(Al.list_of_nuts, 111)
print(Al.all_nuts_tags, 111)

print(Lb.list_of_tags, 111)
Al.all_nut_appender(list_of_nuts=Lb)

print(Al.list_of_nuts, 111)

print("\n")
print(Al.all_nuts_tags)
print(Al.sorted_by_date())
print(Al.searcher("#Futures_plans"), "what")

print(La.give_prevue(n=100, give_text=False))

List_of_Nu = List_of_NuT()
List_of_Nu.NuTs_appender(message="lol", type=2)
List_of_Nu.NuTs_appender(message="e #lole", type=3)

print(List_of_Nu.list_of_nuts[0].message)



# Al.save_file_by_pikle(Al)

# Bl = Al.load_file_by_pikle()

# print(Bl.searcher("#wow"), "wtf")

# print(Al.give_stats())
