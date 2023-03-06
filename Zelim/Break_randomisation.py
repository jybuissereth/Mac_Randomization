import csv
import math
import sys
from collections import defaultdict

def fctTempsOcc(filename,i2):
    """
    :param filename: path vers le fichier qui contient des lignes, chaque ligne a une adresse mac (name) separer par des ';'
    :return: un dictionnaire qui possede comme clé des adresse Mac, et comme valeur (moyenne ifat, nombre d'occurence des trammes asscoiées, dernier temp d'arriver)

        On initilise un dictionnaire vide ou on va stocker des adresses mac et le temps moyern  d'arriver,
    nombre d'occurences des trames , dernier temps d'arriver.

        Lit le fichier d'input qui  contient des lignes, chaque ligne a une adresse mac ( name) seprarer par une ";" et
    de le dernier temps d'arrirver (time).

        Si l'addresse mac est deja presente dans notre dictionnaire on fais un unpacking  puis on calcule the new temps
    moyeen, le nbr d'occurences est  incrementer par 1.
+
        Sinon si c'est la premiere fois bah le temps moyen d'arriver et le dernier tempos d'arriver sont les memes ainsi
    que le  nbr d'occurence et dee 1 vue que c'est la premiere fois qu'on la rencontre.
    """
    D = {}
    with open(filename, 'r') as text_file:
        i=0
        reader = csv.reader(text_file, delimiter=';')
        for ligne in reader:
            if i>i2:
                for key,value in list(D.items()):
                    if value[0]==0:
                        del D[key]
                return D
            time = float(ligne[0])
            name = ligne[1]
            if name in D:
                avg, nb, max_time = D[name]
                avg = (avg * (nb-1) + (time-max_time)) /nb
                nb += 1
                D[name] = (avg, nb, max_time)
            else:
                D[name] = (0, 1, time)
            i+=1
    for key, value in list(D.items()):
        if value[0] == 0:
            del D[key]
    return D

def afficher(d):
    for key, value in d.items():
        print(key, ":", value)

def fctMoy(dict):
  """
    :param dict: un dictionnaire qui posséde comme clé des adresse MAC et comme valeur un tuple (moy ifat, nombre d'occurence, dernier temp d'arriver)
    :return: un dictionnaire qui posséde comme clé des adresse MAC et comme valeur un tuple (moy ifat, ratio, signature de Burst)

        Regroupe les moyennes, occurrence et dernier temps selon leurs burst
    [ partie entière du dernier temps car 1 burst c’est 1 s et les trames sont d’une adresse mac dans 10ms]
    si la partie entière inferieur de chaque dernier temps d'arriver est dans la moyenne d'IFAT
    on prend le tableau des avg_times avec les meme derniers temps d'arrivés et on ajoute l'adresse
    MAC dans le tableau, sinon on ajoute direct l'adresse MAC.

        Ensuite on calcule le ratio (le nombre de d’occurence de trame d’une mac sur le nb totale de trame dans le burst)
    et apres on associe chaque adresse mac a son burst et son ration et temp moyenne d'arriver.

    """
    result = {}
    avg_times = {}
    for key, value in dict.items():
        avg, nb, dT = value
        if math.floor(dT) in avg_times:
            d=avg_times[math.floor(dT)]
            d.append(key)
            avg_times[math.floor(dT)]=d
        else:
            avg_times[math.floor(dT)] = [key]

    for a,li in avg_times.items():
        nb_sum = 0
        for key in li:
            if key in dict:
                avg,nb,dT=dict[key]
                nb_sum+=nb
        for key in li:
            if key in dict:
                avg,nb,dT=dict[key]
                moy = nb / nb_sum
                result[key] = (avg, moy,math.floor(dT))

    return result

"""def fctDistance2(Dict,A,B,c):
    if(Dict[B][2]==Dict[A][2]):
        return  abs(Dict[B][1] - (Dict[A][1]) + (Dict[B][1] + Dict[A][1]) / 2) * abs((Dict[B][0] - Dict[A][0]))
        if((A=='1B:B5:91:85:11:ED' and B=='73:0D:9F:5A:5C:8E') or (B=='1B:B5:91:85:11:ED' and A=='73:0D:9F:5A:5C:8E')):
            a= c * (abs(Dict[B][1] - Dict[A][1]) + (((Dict[B][1] + Dict[A][1]) / 2) * abs(Dict[B][0] - Dict[A][0])))
            print(a)
        return c * (abs(Dict[B][1] - Dict[A][1]) + (((Dict[B][1] + Dict[A][1]) / 2) * abs(Dict[B][0] - Dict[A][0])))

    return (1 - Dict[A][1]) * (abs(Dict[B][1]) + (Dict[B][1] / 2) * abs(Dict[B][0]) + (abs(Dict[A][1]) + (Dict[A][1]) / 2) * abs(Dict[A][0]))
    return abs(Dict[B][1]) + (Dict[B][1] / 2) * abs(Dict[B][0]) + abs((Dict[A][1]) + (Dict[A][1]) / 2) * abs(Dict[A][0])"""

def fctDistance(Dict,A,B,c):

   """
    :param Dict: un dictionnaire qui posséde comme clé des adresse MAC et comme valeur un tuple (moyenne ifat, ratio, signature de Burst)
    :param A: une adresse MAC
    :param B: une adresse MAC
    :param con: une constante fixé par l'utilisateur
    :return: Distance entre l'adresse MAC A et l'adresse MAC B
    """
    
    if ((A == '1B:B5:91:85:11:ED' and B == '73:0D:9F:5A:5C:8E') or (
            B == '1B:B5:91:85:11:ED' and A == '73:0D:9F:5A:5C:8E')):
        a = c * (abs(Dict[B][1] - Dict[A][1]) + (((Dict[B][1] + Dict[A][1]) / 2) * abs(Dict[B][0] - Dict[A][0])))
        print("ICI")
        print(a)
    return c * (abs(Dict[B][1] - Dict[A][1]) + (((Dict[B][1] + Dict[A][1]) / 2) * abs(Dict[B][0] - Dict[A][0])))

def fctDistanceMin(dict,S,list,dict2,t,c):
 """
    :param dict: Un dictionnaire qui posséde comme clé des adresse MAC et comme valeur un tuple (moyenne ifat, ratio, signature de Burst)
    :param S: Une adresse Mac
    :param list: List des adresses Mac déjà rencontré
    :param dict2: Le dictionnaire d’association d’adresse mac(exclu l'addresse MAC S)
    :param t: Parametre fixé l'utilisateur
    :param c: Parametre fixé l'utilisateur
    :return: Un dictionnaire

    La fonction "min" prend en paramètre un dictionnaire, une adresse MAC S, une liste d'adresses MAC déjà rencontrées,
    un second dictionnaire d'association d'adresses MAC (à l'exception de l'adresse MAC S), et les facteurs t et c qui
    sont choisis par l'utilisateur en fonction du document. La fonction calcule la distance minimale entre S et
    le groupe d'adresses MAC déjà rencontrées en utilisant la fonction "distance_deja_vue". Ensuite, elle compare
    cette distance minimale au facteur t. Si la distance minimale est inférieure à t, cela signifie que S et le groupe
    d'adresses MAC déjà rencontrées sont les mêmes adresses. Sinon, ils sont différents et l'adresse S est marquée
    comme ayant déjà été rencontrée.
    """
    s = ((key,fctDistance(dict,S,key,c)) for key in list)
    dmin = min(s, key=lambda x: x[1], default=(None, float('inf')))
    if dmin[1] < t:
        print("\n")
        print("\n")
        print("\n")
        print(S)
        print(dmin)
        print("\n")
        print("\n")
        print("\n")
        dict2[S]=dict2[dmin[0]]
    else:
        dict2[S] = S
    return dict2

def compare_dictionnaires(dict1, dict2):
"""
    :param dict1: un dictionnaire qui associe deux adresses MAC, les données réel
    :param dict2: un dictionnaire qui associe deux adresses MAC, les resultats de notre algorithme
    :return: information sur le taux de success
    """
    non_associe=0
    bonne_assoc=0
    mauvaise_assoc=0
    for key,value in dict1.items():
        if key==value:
            non_associe += 1
        elif dict2[key] == dict2[value]:
            bonne_assoc += 1
        else :
            """print(key)
            print("\n")
            print(value)"""
            mauvaise_assoc +=1
    print("non_assoc")
    print(non_associe)
    print("\n")
    print("bonne_assoc")
    print(bonne_assoc)
    print("\n")
    print("mauvaise_assoc")
    print(mauvaise_assoc)
    print("\n")

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


def main():
    i =0
    Data = fctTempsOcc("donnee",5000)

    Data = fctMoy(Data)
    print(Data)
    Data2=ouvrir("rando_dataset_label")
    A={}
    D=[]
    print(len(Data))
    for key in Data.keys():
        A=fctDistanceMin(Data,key,D,A,0.4,7)
        D.append(key)
        i+=1
        if(i%500==0):
            print(i)
        if i>len(Data):
            raise Exception("Sorry,too much")
    compare_dictionnaires(A,Data2)



main()


