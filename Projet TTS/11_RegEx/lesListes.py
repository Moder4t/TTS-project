# -*- coding: utf-8 -*-
'''
Created on 1 sept. 2021

@author: gills

!!! Attention aux majuscules et minuscules !!!

'''
import re

phrases = [u"quelle heure est-il?", u"il est quelle heure?", u"quel temps fait-il?", u"quelles sont les prévision météo?", u"quelles sont les prévisions de la météo?"]
modeles =["(.)*quelle\sheure(.)*", "(.)*quelle\sheure(.)*", "(.)*quel\stemps(.)*", u"(.)*quelle\ssont\s(.)*prévision(.)*", u"(.)*quelles\ssont\s(.)*prévisions(.)*"]

for i in range(len(phrases)):
    print(phrases[i], modeles[i])
    print()

maPhrase = u"quel temps fait-il?"
#maPhrase = u"quel temps il fait?"

for i in range(len(phrases)):
    if re.match(modeles[i], maPhrase) is not None:
        print("J'ai trouvé!!! ", phrases[i])
        break