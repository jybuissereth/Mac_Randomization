from typing import Dict, List
import string
import random
import sys
import csv
"""def random_mac_breaking(G: List[List[int]], t: int, d: Callable[[List[int], List[int]], int]) -> Dict[int, int]:
  A = {} # Dictionnaire d'alias
  D = [] # Base de données de signatures
  for B in G:
    S = signature(B)
    dmin = float('inf') # On initialise dmin à +infini
    for S0 in D:
      dmin = min(dmin, d(S, S0))
    if dmin < t:
      A[B.mac] = A[S0.mac]
    else:
      A[B.mac] = B.mac
    D.append(S)
  return A"""


## Fonction qui va ouvrir le fichier et affecter les adresses mac randommisé en tant que clef aux vrais adresses mac en tant que valeurs
def ouvrir(file):
    data = {}
    try:
        f = open(file, "r")
        for line in f:
            key, value = line.strip().split(';')
            data[key] = value
        f.close()
        return data
    except FileNotFoundError:
        print('Fichier introuvable')
        sys.exit(0)




## Fonction qui va tester l'égalité entre deux dictionnaires d'adresse mac et renvoyer le pourcentage de bonne association
## PASSER EN PREMIER PARAMETRES LE BON DICIONNAIRE
def compare_dictionnaires(dict1, dict2):
    clefs_com = set(dict1.keys()) & set(dict2.keys())
    nb_clefs = len(dict1)
    val_com = sum(dict1.get(key) == dict2.get(key) for key in clefs_com)
    result = (val_com / nb_clefs) *100
    print("Les deux dictionnaires sont égaux à ", result, "%")

def afficher(Dict):
    for key, value in Dict.items():
        print(key, ":", value)

"""
A= {"A": 1, "B": 1, "C": 1, "D": 1, "E": 1, "F": 1,"Z": 1, "T": 3,"H":7,"R":7}
B= {"A": 5, "B": 1, "C": 2, "D": 1, "F": 3, "Z": 2}
compare_dictionnaires(A,B)
"""


D=ouvrir("rando_dataset_label")
afficher(D)