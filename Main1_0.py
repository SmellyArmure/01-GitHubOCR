from math import *
import random

nbeFrTemp = ""
nbeNumTemp = 0
dicoFrNum = {} # dictionnaire Français vers Numérique
listFrNum = [] # liste à 2 dimensions
listFrNumTrans = []

#---- Lit un fichier texte dictionnaire
fichierDico = open("Fichier_Dico_FrNum.txt","r") # lecture
listDico = fichierDico.readlines() # liste à 1 dimension

#---- Découpe le dictionnaire pour alimenter un tableau
for i in range(0,len(listDico)):
    listDico[i] = listDico[i].strip() # retire les retours chariot
    listFrNum.append(listDico[i].split()) # découpe les lignes en mots et écrit toutes les entrées

listFrNum = sorted(listFrNum) # trie les entrées suivant la première colonne et remplace
listFrNumTrans = [[row[i] for row in listFrNum] for i in range(len(listFrNum[0]))] # transpose

print(listFrNum)

fichierDico.close()