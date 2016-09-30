__author__ = 'williamscullion'

import pickle
import urllib.request as req

web_banner = req.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
un_pickled = pickle.load(web_banner)

print(un_pickled)

for liste_de_lignes in un_pickled:
    ligne = [lettre * nb for lettre, nb in liste_de_lignes]
    print("".join(ligne))